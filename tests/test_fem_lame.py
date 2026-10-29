"""Verifica del solutore FEM sul problema di Lamé.

Il FEM deve riprodurre la soluzione analitica di src/aorta/analytical/lame.py:
errore sotto l'1% su una mesh grossolana, e errore che cala in fretta
quando si raffina la mesh (convergenza).

Uso:
    conda activate cardio
    pytest tests/test_fem_lame.py -v
"""

import numpy as np
import ufl
from dolfinx import fem, mesh
from mpi4py import MPI

from aorta.analytical.lame import radial_displacement
from aorta.fem.linear_elasticity import epsilon, relative_l2_error, solve_pressurized_ring
from aorta.mesh.annulus import quarter_annulus

# stessi valori di test_lame.py: aorta toracica
A, B = 12.5e-3, 14.5e-3  # raggi interno ed esterno [m]
P = 16_000.0  # pressione interna [Pa], circa 120 mmHg
E, NU = 1.0e6, 0.45  # modulo di Young [Pa] e coefficiente di Poisson [-]


def test_rotazione_rigida_non_deforma():
    # u = (-y, x) è una rotazione rigida: sposta i punti ma non deforma, quindi ε = 0.
    # Serve perché la soluzione di Lamé, essendo radiale, non distingue grad(u) da sym(grad(u)).
    domain = mesh.create_unit_square(MPI.COMM_WORLD, 4, 4)
    x = ufl.SpatialCoordinate(domain)
    rotazione = ufl.as_vector((-x[1], x[0]))
    eps = epsilon(rotazione)
    assert abs(fem.assemble_scalar(fem.form(ufl.inner(eps, eps) * ufl.dx))) < 1e-12


def errore_fem(h):
    """Risolve con passo di mesh h e restituisce l'errore relativo sullo spostamento."""
    domain, facet_tags = quarter_annulus(A, B, h)
    uh = solve_pressurized_ring(domain, facet_tags, P, E, NU)

    # soluzione esatta come campo vettoriale: u = u_r(r) * (x, y) / r
    x = ufl.SpatialCoordinate(domain)
    r = ufl.sqrt(x[0] ** 2 + x[1] ** 2)
    u_exact = radial_displacement(r, A, B, P, E, NU) / r * x
    return relative_l2_error(uh, u_exact)


def test_errore_sotto_1_percento():
    # mesh grossolana: 4 elementi nello spessore della parete
    assert errore_fem(h=(B - A) / 4) < 0.01


def test_convergenza():
    # dimezzando il lato degli elementi l'errore deve calare almeno di 2^2.5 ≈ 5.7 volte
    # (con elementi quadratici la teoria prevede 2^3 = 8)
    e1, e2 = errore_fem(h=(B - A) / 2), errore_fem(h=(B - A) / 4)
    ordine = np.log2(e1 / e2)
    assert ordine > 2.5
