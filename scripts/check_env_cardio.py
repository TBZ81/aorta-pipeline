"""Verifica dell'ambiente `cardio` (FEM/CFD).

Risolve un problema di Poisson in 3D con soluzione nota, u = 1 + x^2 + 2y^2 + 3z^2,
e controlla che l'errore numerico sia ~0 (la soluzione è quadratica, quindi
elementi P2 la rappresentano esattamente). Testa anche gmsh e la lettura
di una mesh gmsh in dolfinx.

Uso:
    conda activate cardio
    mpirun -n 4 python scripts/check_env_cardio.py
"""

import time

import dolfinx
import gmsh
import numpy as np
import ufl
from dolfinx import fem, mesh
from dolfinx.fem.petsc import LinearProblem
from dolfinx.io import gmsh as gmshio
from mpi4py import MPI


def poisson_test():
    comm = MPI.COMM_WORLD
    domain = mesh.create_unit_cube(comm, 16, 16, 16)
    V = fem.functionspace(domain, ("Lagrange", 2))

    x = ufl.SpatialCoordinate(domain)
    u_exact = 1 + x[0] ** 2 + 2 * x[1] ** 2 + 3 * x[2] ** 2
    f = -ufl.div(ufl.grad(u_exact))

    u_bc = fem.Function(V)
    u_bc.interpolate(lambda p: 1 + p[0] ** 2 + 2 * p[1] ** 2 + 3 * p[2] ** 2)
    domain.topology.create_connectivity(domain.topology.dim - 1, domain.topology.dim)
    boundary_dofs = fem.locate_dofs_topological(
        V, domain.topology.dim - 1, mesh.exterior_facet_indices(domain.topology)
    )
    bc = fem.dirichletbc(u_bc, boundary_dofs)

    u, v = ufl.TrialFunction(V), ufl.TestFunction(V)
    a = ufl.inner(ufl.grad(u), ufl.grad(v)) * ufl.dx
    L = f * v * ufl.dx
    problem = LinearProblem(
        a, L, bcs=[bc], petsc_options_prefix="poisson",
        petsc_options={"ksp_type": "cg", "pc_type": "hypre", "ksp_rtol": 1e-12},
    )
    t0 = time.perf_counter()
    uh = problem.solve()
    elapsed = time.perf_counter() - t0

    err_local = fem.assemble_scalar(fem.form((uh - u_exact) ** 2 * ufl.dx))
    err = np.sqrt(comm.allreduce(err_local, op=MPI.SUM))
    ndofs = V.dofmap.index_map.size_global
    return err, ndofs, elapsed


def gmsh_test():
    """Crea un cilindro (un 'vaso' ideale) con gmsh e lo carica in dolfinx."""
    comm = MPI.COMM_WORLD
    gmsh.initialize()
    gmsh.option.setNumber("General.Terminal", 0)
    if comm.rank == 0:
        gmsh.model.add("tubo")
        vol = gmsh.model.occ.addCylinder(0, 0, 0, 0, 0, 0.1, 0.01)  # L=10 cm, R=1 cm
        gmsh.model.occ.synchronize()
        gmsh.model.addPhysicalGroup(3, [vol], tag=1)
        gmsh.option.setNumber("Mesh.CharacteristicLengthMax", 0.002)
        gmsh.model.mesh.generate(3)
    mesh_data = gmshio.model_to_mesh(gmsh.model, comm, 0, gdim=3)
    gmsh.finalize()
    domain = mesh_data.mesh
    n_cells = domain.topology.index_map(3).size_global
    volume = comm.allreduce(
        fem.assemble_scalar(fem.form(1.0 * ufl.dx(domain=domain))), op=MPI.SUM
    )
    return n_cells, volume


if __name__ == "__main__":
    rank = MPI.COMM_WORLD.rank
    nproc = MPI.COMM_WORLD.size

    err, ndofs, elapsed = poisson_test()
    n_cells, volume = gmsh_test()
    exact_volume = np.pi * 0.01**2 * 0.1

    if rank == 0:
        print(f"dolfinx {dolfinx.__version__} | gmsh {gmsh.__version__} | processi MPI: {nproc}")
        print(f"[Poisson] gradi di libertà: {ndofs:,} | errore L2: {err:.2e} | tempo: {elapsed:.2f} s")
        print(f"[gmsh]    tetraedri: {n_cells:,} | volume: {volume:.4e} m^3 "
              f"(esatto {exact_volume:.4e}, diff {abs(volume - exact_volume) / exact_volume:.2%})")
        ok = err < 1e-8 and abs(volume - exact_volume) / exact_volume < 0.01
        print("ESITO:", "OK" if ok else "PROBLEMA")
