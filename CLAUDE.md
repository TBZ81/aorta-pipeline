# aorta-pipeline — istruzioni per Claude Code

## Obiettivo
Pipeline cardiovascolare open source sull'aorta: TC angiografica → segmentazione AI → geometria e mesh → CFD (emodinamica: WSS, OSI, pressione) e FEM (stress di parete iperelastico) → modello AI surrogato. Progetto portfolio (GitHub/LinkedIn): ogni fase deve produrre un risultato **misurabile** e verificato.

## Chi lavora qui
Ingegnere biomedico (biomeccanica e biomateriali), principiante con Python, VS Code, git e Claude Code. Rispondere in italiano, spiegare cosa fa il codice e perché, procedere a piccoli passi, far eseguire all'utente i comandi chiave.

## Ambienti (Miniforge, `~/miniforge3`)
- `cardio` (`environment.yml`): FEniCSx (dolfinx), gmsh, OpenMPI, PyVista, meshio. Per FEM, CFD, mesh.
- `cardio-ai` (`environment-ai.yml`): PyTorch (conda-forge, con GPU Apple MPS), TotalSegmentator. Per imaging e AI.
- Verifica: `python scripts/check_env_cardio.py` (anche con `mpirun -n 4`) e `python scripts/check_env_ai.py`.

## Vincoli hardware e software (MacBook Pro M1 Pro, 16 GB RAM, nessuna CUDA)
- Mesh CFD entro circa 1M di tetraedri, solutori iterativi (niente solutori diretti su problemi 3D grandi).
- In parallelo usare `mpirun -n 4` (4–6 processi).
- AI: modelli preaddestrati o piccoli; niente addestramento 3D da zero.
- Usare OpenMPI, non MPICH: MPICH su questo Mac passa dalle interfacce VPN ed è lentissimo.
- Installare PyTorch da conda-forge, non da pip: la versione pip carica una seconda copia di OpenMP e va in crash.
- Rosetta non installato: niente binari x86_64 (VMTK su conda esiste solo x86_64 su macOS).

## Scelte di strumenti
Solo open source, consolidati e stato dell'arte. Preferire pacchetti nativi arm64.

## Convenzioni
- Unità SI nel codice (m, Pa, s, kg/m³); conversioni (mmHg, cm) solo in input e output.
- Codice riutilizzabile in `src/`, test in `tests/`, script eseguibili in `scripts/`, esplorazione in `notebooks/`.
- I dati in `data/` e i risultati pesanti non vanno nel repo: ogni dataset deve avere uno script di download e la licenza citata nel README.
- Ogni solutore va verificato con una soluzione analitica prima di usarlo su geometrie reali.

## Fasi
0 setup · 1 FEM di base (Lamé) · 2 CFD di base (Poiseuille, Womersley) · 3 segmentazione AI (AVT, Dice/HD95) · 4 geometria → mesh · 5 CFD su paziente reale · 6 FEM della parete · 7 surrogato AI.
