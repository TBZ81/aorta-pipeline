"""Elasticità lineare 2D in deformazione piana: anello sotto pressione interna.

Forma debole: trovare u tale che, per ogni funzione test v,
    ∫ σ(u) : ε(v) dx = ∫ t · v ds,    con t = -p_i n sul bordo interno,
dove n è la normale uscente dal dominio (sul bordo interno punta verso il centro,
quindi -p_i n spinge la parete verso l'esterno).
"""

import dolfinx
import numpy as np
import ufl
from dolfinx import fem, mesh
from dolfinx.fem.petsc import LinearProblem
from mpi4py import MPI

from aorta.mesh.annulus import BOTTOM, INNER, LEFT


def lame_parameters(E, nu):
    """Parametri di Lamé (lambda, mu) [Pa] da modulo di Young e coefficiente di Poisson."""
    lmbda = E * nu / ((1 + nu) * (1 - 2 * nu))
    mu = E / (2 * (1 + nu))
    return lmbda, mu


def epsilon(u):
    """Tensore delle piccole deformazioni."""
    return ufl.sym(ufl.grad(u))


def sigma(u, lmbda, mu):
    """Tensore delle tensioni, legge di Hooke per materiale isotropo."""
    return lmbda * ufl.tr(epsilon(u)) * ufl.Identity(u.ufl_shape[0]) + 2 * mu * epsilon(u)


def solve_pressurized_ring(domain, facet_tags, p_i, E, nu, degree=2):
    """Risolve il quarto di anello in pressione e restituisce lo spostamento u [m]."""
    lmbda, mu = lame_parameters(E, nu)
    V = fem.functionspace(domain, ("Lagrange", degree, (domain.geometry.dim,)))
    u, v = ufl.TrialFunction(V), ufl.TestFunction(V)

    # simmetria: u_y = 0 sul bordo y = 0, u_x = 0 sul bordo x = 0
    fdim = domain.topology.dim - 1
    zero = dolfinx.default_scalar_type(0.0)
    bcs = []
    for tag, component in ((BOTTOM, 1), (LEFT, 0)):
        dofs = fem.locate_dofs_topological(V.sub(component), fdim, facet_tags.find(tag))
        bcs.append(fem.dirichletbc(zero, dofs, V.sub(component)))

    n = ufl.FacetNormal(domain)
    ds = ufl.Measure("ds", domain=domain, subdomain_data=facet_tags)
    # lavoro virtuale interno (a) ed esterno (L)
    a = ufl.inner(sigma(u, lmbda, mu), epsilon(v)) * ufl.dx
    L = ufl.dot(-p_i * n, v) * ds(INNER)

    problem = LinearProblem(
        a, L, bcs=bcs, petsc_options_prefix="anello",
        petsc_options={"ksp_type": "preonly", "pc_type": "lu", "pc_factor_mat_solver_type": "mumps"},
    )
    return problem.solve()


def relative_l2_error(uh, u_exact):
    """Errore relativo in norma L2: ||uh - u_exact|| / ||u_exact||."""
    comm = uh.function_space.mesh.comm
    error = fem.assemble_scalar(fem.form(ufl.inner(uh - u_exact, uh - u_exact) * ufl.dx))
    norm = fem.assemble_scalar(fem.form(ufl.inner(u_exact, u_exact) * ufl.dx))
    return np.sqrt(comm.allreduce(error, op=MPI.SUM) / comm.allreduce(norm, op=MPI.SUM))
