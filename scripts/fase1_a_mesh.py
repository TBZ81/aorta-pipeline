"""Fase 1, passo 4a: guardare la mesh del quarto di anello.

Crea la mesh, stampa qualche numero e salva un'immagine in results/fase1/mesh.png.

Uso (dalla cartella del progetto):
    conda activate cardio
    python scripts/fase1_a_mesh.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from aorta.mesh.annulus import quarter_annulus

# 1. dati del problema: aorta toracica (in metri, come sempre nel codice)
A = 12.5e-3  # raggio interno [m]
B = 14.5e-3  # raggio esterno [m]
H = (B - A) / 4  # lato degli elementi: 4 elementi nello spessore della parete

# 2. creare la mesh
domain, facet_tags = quarter_annulus(A, B, H)

# 3. leggere i nodi e i triangoli
xy = domain.geometry.x[:, :2] * 1e3  # coordinate dei nodi, in mm per il grafico
triangoli = domain.geometry.dofmaps[0]  # ogni riga: i 6 nodi di un triangolo quadratico
vertici = triangoli[:, :3]  # i primi 3 nodi sono i vertici
nodi_medi = triangoli[:, 3:]  # gli altri 3 stanno a metà dei lati

print("MESH DEL QUARTO DI ANELLO")
print(f"  raggio interno     a = {A * 1e3:.1f} mm")
print(f"  raggio esterno     b = {B * 1e3:.1f} mm")
print(f"  spessore parete  b-a = {(B - A) * 1e3:.1f} mm")
print(f"  lato elementi      h = {H * 1e3:.2f} mm")
print(f"  triangoli            = {len(triangoli)}")
print(f"  nodi in tutto        = {len(xy)}")
print("  nodi per triangolo   = 6 (3 vertici + 3 a metà dei lati)")

# 4. disegnare tre riquadri, da leggere da sinistra a destra
a, b = A * 1e3, B * 1e3  # raggi in mm per il disegno
theta = np.linspace(0, np.pi / 2, 100)  # angoli da 0 a 90 gradi
fig, (r1, r2, r3) = plt.subplots(1, 3, figsize=(19, 6.5))

# riquadro 1: la sezione intera dell'aorta e il quarto che modelliamo
giro = np.linspace(0, 2 * np.pi, 300)
r1.fill(b * np.cos(giro), b * np.sin(giro), color="lightgray")  # parete
r1.fill(a * np.cos(giro), a * np.sin(giro), color="mistyrose")  # lume, pieno di sangue
r1.fill(np.r_[a * np.cos(theta), b * np.cos(theta[::-1])],
        np.r_[a * np.sin(theta), b * np.sin(theta[::-1])], color="lightcoral")
r1.text(0, 0, "lume\n(sangue)", ha="center", va="center", fontsize=12)
r1.text(-b * 0.75, -b * 0.75, "parete", fontsize=12)
r1.annotate("modelliamo\nsolo questo quarto", xy=(b * 0.6, b * 0.6), xytext=(-b * 0.1, b * 0.35),
            fontsize=12, color="firebrick", arrowprops={"arrowstyle": "->", "color": "firebrick"})
r1.set_title("1. Sezione dell'aorta (Ø 25 mm, parete 2 mm)")

# riquadro 2: la mesh del quarto, con vincoli e carico sui 4 bordi
r2.triplot(xy[:, 0], xy[:, 1], vertici, color="gray", linewidth=0.4)
r2.plot(a * np.cos(theta), a * np.sin(theta), color="red", linewidth=4, label="interno: pressione 120 mmHg")
r2.plot(b * np.cos(theta), b * np.sin(theta), color="green", linewidth=4, label="esterno: libero")
r2.plot([a, b], [0, 0], color="blue", linewidth=4, label="sotto: simmetria, scorre solo in x")
r2.plot([0, 0], [a, b], color="purple", linewidth=4, label="sinistra: simmetria, scorre solo in y")
for t in np.linspace(0.1, 1.47, 8):  # frecce della pressione, spingono la parete verso fuori
    r2.annotate("", xy=(a * np.cos(t), a * np.sin(t)), xytext=(0.7 * a * np.cos(t), 0.7 * a * np.sin(t)),
                arrowprops={"arrowstyle": "->", "color": "red", "linewidth": 1.5})
r2.add_patch(plt.Rectangle((12, 0), 3, 3, fill=False, color="black", linewidth=2, linestyle="--"))
r2.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), fontsize=10)
r2.set_title(f"2. Mesh ({len(triangoli)} triangoli, {len(xy)} nodi), vincoli e carico")

# riquadro 3: zoom (riquadro tratteggiato), con un triangolo evidenziato e i suoi 6 nodi
r3.triplot(xy[:, 0], xy[:, 1], vertici, color="black", linewidth=0.6)
r3.plot(xy[vertici.ravel(), 0], xy[vertici.ravel(), 1], "o", color="navy", markersize=6, label="vertici")
r3.plot(xy[nodi_medi.ravel(), 0], xy[nodi_medi.ravel(), 1], "o", color="orange", markersize=4,
        label="nodi a metà lato")
centri = xy[vertici].mean(axis=1)
scelto = np.argmin(np.hypot(centri[:, 0] - 13.5, centri[:, 1] - 1.5))  # il triangolo vicino a (13.5, 1.5)
r3.fill(xy[vertici[scelto], 0], xy[vertici[scelto], 1], color="gold", alpha=0.6)
for numero, nodo in enumerate(triangoli[scelto], start=1):
    r3.text(xy[nodo, 0] + 0.03, xy[nodo, 1] + 0.03, str(numero), fontsize=13, fontweight="bold")
for x0, testo in ((a, "r = 12,5 mm"), (b, "r = 14,5 mm")):
    r3.text(x0, -0.22, testo, ha="center", fontsize=10)
r3.annotate("", xy=(a, -0.42), xytext=(b, -0.42), arrowprops={"arrowstyle": "<->"})
r3.text((a + b) / 2, -0.7, "parete: 2 mm = 4 triangoli", ha="center", fontsize=11)
r3.set_xlim(12, 15)
r3.set_ylim(-0.8, 3.0)
r3.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, fontsize=10)
r3.set_title("3. Zoom: un triangolo (giallo) ha 6 nodi")

for ax in (r1, r2, r3):
    ax.set_aspect("equal")
    ax.set_xlabel("x [mm]")
    ax.set_ylabel("y [mm]")

cartella = Path("results/fase1")
cartella.mkdir(parents=True, exist_ok=True)
fig.savefig(cartella / "mesh.png", dpi=100, bbox_inches="tight")
print(f"\nImmagine salvata in {cartella / 'mesh.png'}")
