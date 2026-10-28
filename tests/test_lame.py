"""Test della soluzione di Lamé.

I test non ripetono le formule: controllano che rispettino la fisica
(condizioni al contorno, equilibrio, legge di Hooke, limite di parete sottile).
Se un test fallisce, il nome dice quale principio fisico non è rispettato.

Uso:
    conda activate cardio
    pytest tests/test_lame.py -v
"""

import numpy as np
import pytest

from aorta.analytical.lame import radial_displacement, sigma_r, sigma_theta

# Aorta toracica, ordini di grandezza realistici
A = 12.5e-3  # raggio interno [m]
B = 14.5e-3  # raggio esterno [m] (parete di 2 mm)
P = 16_000.0  # pressione interna [Pa], circa 120 mmHg
E = 1.0e6  # modulo di Young [Pa]
NU = 0.45  # coefficiente di Poisson [-]

R = np.linspace(A, B, 201)  # raggi a cui controllare la soluzione


# --- Esercizio 1: tensioni -------------------------------------------------


def test_bordo_interno_pressione_applicata():
    # sulla superficie interna la tensione radiale è la pressione, con segno meno
    assert sigma_r(A, A, B, P) == pytest.approx(-P)


def test_bordo_esterno_scarico():
    # la superficie esterna è libera: tensione radiale nulla
    assert sigma_r(B, A, B, P) == pytest.approx(0.0, abs=1e-9 * P)


def test_equilibrio_radiale():
    # equilibrio in coordinate cilindriche: d(r * sigma_r)/dr = sigma_theta
    d_r_sigma_r = np.gradient(R * sigma_r(R, A, B, P), R)
    np.testing.assert_allclose(d_r_sigma_r[1:-1], sigma_theta(R, A, B, P)[1:-1], rtol=1e-4)


def test_limite_parete_sottile():
    # se la parete è sottilissima vale la formula di Mariotte: sigma_theta = p * r / t
    a, b = 12.5e-3, 12.5e-3 * 1.001
    r_medio, t = (a + b) / 2, b - a
    assert sigma_theta(r_medio, a, b, P) == pytest.approx(P * r_medio / t, rel=1e-3)


def test_funziona_con_array():
    assert sigma_r(R, A, B, P).shape == R.shape
    assert sigma_theta(R, A, B, P).shape == R.shape


# --- Esercizio 2: spostamento ---------------------------------------------


def test_hooke_deformazione_circonferenziale():
    # in deformazione piana: eps_theta = u/r = (1+nu)/E * ((1-nu) sigma_theta - nu sigma_r)
    eps_theta = radial_displacement(R, A, B, P, E, NU) / R
    hooke = (1 + NU) / E * ((1 - NU) * sigma_theta(R, A, B, P) - NU * sigma_r(R, A, B, P))
    np.testing.assert_allclose(eps_theta, hooke, rtol=1e-10)


def test_hooke_deformazione_radiale():
    # in deformazione piana: eps_r = du/dr = (1+nu)/E * ((1-nu) sigma_r - nu sigma_theta)
    eps_r = np.gradient(radial_displacement(R, A, B, P, E, NU), R)
    hooke = (1 + NU) / E * ((1 - NU) * sigma_r(R, A, B, P) - NU * sigma_theta(R, A, B, P))
    np.testing.assert_allclose(eps_r[1:-1], hooke[1:-1], rtol=1e-4)
