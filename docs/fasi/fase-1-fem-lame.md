# Fase 1: FEM di base, il cilindro di Lamé

**Obiettivo:** verificare il solutore FEM (FEniCSx) su un problema con soluzione esatta: un cilindro a parete spessa sotto pressione interna, cioè un tratto di aorta idealizzato.
**Risultato misurabile:** errore FEM rispetto a Lamé sotto l'1% e curva di convergenza con l'ordine teorico (circa 3 per elementi quadratici).
**Stato:** 🔄 in corso: esercizi 1-3 fatti e su GitHub (commit 653436e), ora **esercizio 4a** (guardare la mesh).

Valori usati (aorta toracica): raggio interno 12,5 mm, parete 2 mm, pressione 16 kPa (circa 120 mmHg), E = 1 MPa, ν = 0,45.

## Esercizi
- [x] **1 · Tensioni di Lamé** 🧑: `sigma_r` e `sigma_theta` in `src/aorta/analytical/lame.py`.
- [x] **2 · Spostamento radiale** 🧑: `radial_displacement` (deformazione piana). I 7 test di `tests/test_lame.py` sono verdi.
- [x] **3 · Il cilindro con FEniCSx** 🧑: in `src/aorta/fem/linear_elasticity.py` sostituire le tre righe `raise NotImplementedError`:
  - 3a: `epsilon(u)`, la deformazione = parte simmetrica del gradiente;
  - 3b: `sigma(u, lmbda, mu)`, la legge di Hooke isotropa;
  - 3c: `a = ...`, la forma bilineare ∫ σ(u) : ε(v) dx.

  Verifica: `pytest tests/test_fem_lame.py -v` dà **3 passed** (fatto il 29/10). Ricorda di attivare prima `conda activate cardio`: in `(base)` pytest non c'è.
  Comandi UFL usati: `ufl.grad`, `ufl.sym`, `ufl.tr`, `ufl.Identity`, `ufl.inner`, `ufl.dx`.
- [x] **Commit e Sync** 🧑: messaggio suggerito `Fase 1: solutore FEM per il cilindro di Lamé`. Includi anche `.gitignore`, `environment.yml`, `CLAUDE.md` e `docs/` modificati.
- [ ] **4 · Visualizzare** 🤖 + 🧑, a piccoli passi:
  - [ ] 4a: guardare la mesh, `python scripts/fase1_a_mesh.py` → `results/fase1/mesh.png` (430 triangoli, 955 nodi);
  - [ ] 4b: tabella FEM contro Lamé lungo lo spessore (mm, kPa, errore %);
  - [ ] 4c: salvare i risultati in XDMF e aprirli in ParaView (anello deformato, mappa di σθ).
- [ ] **5 · Notebook della fase** 🧑 guidato: `notebooks/fase1_lame.ipynb` con mesh 3D interattiva, confronto FEM e Lamé lungo lo spessore, curva di convergenza.
- [ ] **6 · Grafico di convergenza nel README** 🤖 + 🧑: script in `scripts/` che salva la figura in `results/fase1/`.
- [ ] **7 · Materiale iperelastico** (neo-Hooke): lo stesso cilindro, non lineare. Prepara la Fase 6.
- [ ] **8 · (facoltativo) Cilindro 3D da FreeCAD** e confronto con CalculiX (vedi [percorso CAD](extra-cad.md)).

## File della fase
| File | Chi l'ha scritto | Cosa fa |
|---|---|---|
| `src/aorta/analytical/lame.py` | 🧑 | soluzione esatta |
| `src/aorta/mesh/annulus.py` | 🤖 | mesh di un quarto di anello (gmsh, triangoli curvi) |
| `src/aorta/fem/linear_elasticity.py` | 🤖 + 🧑 | solutore FEM |
| `tests/test_lame.py`, `tests/test_fem_lame.py` | 🤖 | verifiche fisiche |

## Concetti da studiare
- **Forma debole** ed equazione del lavoro virtuale: ∫ σ(u):ε(v) dx = ∫ t·v ds.
- **Parametri di Lamé** λ e μ, e il loro legame con E e ν.
- **Deformazione piana** (cilindro lungo, εz = 0).
- **Ordine di convergenza:** dimezzando la dimensione degli elementi, con elementi quadratici l'errore cala circa di 2³ = 8 volte.
- **Perché il test della rotazione rigida:** la soluzione di Lamé è radiale e non distingue grad(u) da sym(grad(u)).
