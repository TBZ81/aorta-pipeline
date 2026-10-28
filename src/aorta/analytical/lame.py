"""Soluzione di Lamé: cilindro a parete spessa sotto pressione interna.

Ipotesi: materiale elastico lineare isotropo, pressione interna p_i,
pressione esterna nulla, deformazione piana (cilindro lungo, eps_z = 0).

Simboli (unità SI):
    r    raggio a cui si valuta la soluzione [m] (numero o array numpy)
    a    raggio interno [m]
    b    raggio esterno [m]
    p_i  pressione interna [Pa]
    E    modulo di Young [Pa]
    nu   coefficiente di Poisson [-]

Le funzioni accettano anche array numpy per r: le operazioni come r**2
vengono applicate elemento per elemento.
"""


def sigma_r(r, a, b, p_i):
    """Tensione radiale sigma_r(r) [Pa]."""
    return p_i * a**2 / (b**2 - a**2) * (1 - b**2 / r**2)

 


def sigma_theta(r, a, b, p_i):
    """Tensione circonferenziale sigma_theta(r) [Pa]."""
    return p_i * a**2 / (b**2 - a**2) * (1 + b**2 / r**2)



def radial_displacement(r, a, b, p_i, E, nu):
    """Spostamento radiale u_r(r) [m] in deformazione piana."""
    return (1 + nu) * p_i * a**2 / (E * (b**2 - a**2)) * ((1 - 2 * nu) * r + b**2 / r)
