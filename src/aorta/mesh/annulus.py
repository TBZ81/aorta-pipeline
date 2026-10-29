"""Mesh di un quarto di corona circolare: la sezione di un cilindro a parete spessa.

Per simmetria basta modellare un quarto della sezione (primo quadrante).
I bordi sono etichettati con i tag qui sotto, usati per carichi e vincoli.
"""

import gmsh
from dolfinx.io import gmsh as gmshio
from mpi4py import MPI

# tag dei bordi
INNER = 1  # arco interno r = a (pressione)
OUTER = 2  # arco esterno r = b (libero)
BOTTOM = 3  # segmento sull'asse x, y = 0 (simmetria)
LEFT = 4  # segmento sull'asse y, x = 0 (simmetria)


def quarter_annulus(a, b, h, comm=MPI.COMM_WORLD):
    """Quarto di corona a < r < b con triangoli quadratici di lato circa h [m].

    I triangoli quadratici (6 nodi) seguono la curvatura degli archi, così
    l'errore geometrico non limita la convergenza della soluzione.
    Restituisce (domain, facet_tags).
    """
    gmsh.initialize()
    gmsh.option.setNumber("General.Terminal", 0)
    if comm.rank == 0:
        gmsh.model.add("quarto_di_corona")
        occ = gmsh.model.occ
        ring = occ.cut([(2, occ.addDisk(0, 0, 0, b, b))], [(2, occ.addDisk(0, 0, 0, a, a))])[0]
        quarter = occ.intersect(ring, [(2, occ.addRectangle(0, 0, 0, b, b))])[0]
        occ.synchronize()

        gmsh.model.addPhysicalGroup(2, [quarter[0][1]], tag=1)
        # ogni bordo si riconosce dal suo punto medio
        tol = 1e-6 * b
        for _, curve in gmsh.model.getBoundary(quarter, oriented=False):
            t_min, t_max = gmsh.model.getParametrizationBounds(1, curve)
            x, y, _ = gmsh.model.getValue(1, curve, [(t_min[0] + t_max[0]) / 2])
            if abs(y) < tol:
                tag = BOTTOM
            elif abs(x) < tol:
                tag = LEFT
            elif abs((x**2 + y**2) ** 0.5 - a) < tol:
                tag = INNER
            else:
                tag = OUTER
            gmsh.model.addPhysicalGroup(1, [curve], tag=tag)

        gmsh.option.setNumber("Mesh.MeshSizeMax", h)
        gmsh.option.setNumber("Mesh.MeshSizeMin", h)
        gmsh.model.mesh.generate(2)
        gmsh.model.mesh.setOrder(2)
    mesh_data = gmshio.model_to_mesh(gmsh.model, comm, 0, gdim=2)
    gmsh.finalize()
    return mesh_data.mesh, mesh_data.facet_tags
