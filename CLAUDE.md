# aorta-pipeline — istruzioni per Claude Code

## Obiettivo
Pipeline cardiovascolare open source sull'aorta: TC angiografica → segmentazione AI → geometria e mesh → CFD (emodinamica: WSS, OSI, pressione) e FEM (stress di parete iperelastico) → modello AI surrogato. Progetto portfolio (GitHub/LinkedIn): ogni fase deve produrre un risultato **misurabile** e verificato.

## Chi lavora qui
Ingegnere biomedico (biomeccanica e biomateriali), principiante con Python, VS Code, git e Claude Code. Rispondere in italiano, spiegare cosa fa il codice e perché, procedere a piccoli passi, far eseguire all'utente i comandi chiave.

## Ambienti (Miniforge, `~/miniforge3`)
- `cardio` (`environment.yml`): FEniCSx (dolfinx), gmsh, OpenMPI, PyVista, meshio. Per FEM, CFD, mesh.
- `cardio-ai` (`environment-ai.yml`): PyTorch (conda-forge, con GPU Apple MPS), TotalSegmentator. Per imaging e AI.
- `cardio-vmtk` (x86_64, gira in Rosetta; non ha ancora un file `.yml`): Python 3.11 e VMTK 1.5.0 da conda-forge. Solo per la linea centrale e la preparazione della geometria (Fase 4).
- Verifica: `python scripts/check_env_cardio.py` (anche con `mpirun -n 4`) e `python scripts/check_env_ai.py`.

## Vincoli hardware e software (MacBook Pro M1 Pro, 16 GB RAM, nessuna CUDA)
- Mesh CFD entro circa 1M di tetraedri, solutori iterativi (niente solutori diretti su problemi 3D grandi).
- In parallelo usare `mpirun -n 4` (4–6 processi).
- AI: modelli preaddestrati o piccoli; niente addestramento 3D da zero.
- Usare OpenMPI, non MPICH: MPICH su questo Mac passa dalle interfacce VPN ed è lentissimo.
- Installare PyTorch da conda-forge, non da pip: la versione pip carica una seconda copia di OpenMP e va in crash.
- Rosetta è installato, ma i binari x86_64 vanno limitati a ciò che non esiste per arm64: VMTK (su conda per macOS c'è solo x86_64) e 3D Slicer.

## Scelte di strumenti
Solo open source, consolidati e stato dell'arte. Preferire pacchetti nativi arm64.
- CAD: FreeCAD 1.1.4 (arm64, `/Applications/FreeCAD.app`). Per gli script senza interfaccia: `Contents/Resources/bin/freecadcmd`. Include CalculiX (`ccx`), utile come secondo solutore FEM.
- Visualizzazione: ParaView 6.2.0 per i risultati (arm64, `/Applications/ParaView-6.2.0.app`; per gli script `Contents/bin/pvbatch` e `pvpython`, gli XDMF si leggono con `Xdmf3ReaderS`), PyVista e notebook in VS Code per gli esercizi, gmsh per le mesh.
- Imaging: 3D Slicer 5.12.4 (`/Applications/Slicer.app`). Esiste solo per x86_64, quindi gira in Rosetta.

## Passaggi tra gli strumenti (verificati il 2026-10-28)
- FreeCAD → STEP (in mm) → gmsh con `gmsh.option.setString("Geometry.OCCTargetUnit", "M")` per convertire in metri → dolfinx.
- NIfTI (la maschera di `cardio-ai`, in mm) → `cardio-vmtk` (marching cubes, linea centrale) → superficie `.vtp` o `.stl` in mm: convertire in metri prima di fare la mesh.
- Risultati di dolfinx: `XDMFFile` per ParaView. Per PyVista usare `dolfinx.plot.vtk_mesh` oppure `VTKFile` (.pvd), perché `pyvista.read` non legge gli XDMF che contengono solo la mesh.

## Convenzioni
- Unità SI nel codice (m, Pa, s, kg/m³); conversioni (mmHg, cm) solo in input e output.
- Codice riutilizzabile in `src/`, test in `tests/`, script eseguibili in `scripts/`, esplorazione in `notebooks/`.
- I dati in `data/` e i risultati pesanti non vanno nel repo: ogni dataset deve avere uno script di download e la licenza citata nel README.
- Ogni solutore va verificato con una soluzione analitica prima di usarlo su geometrie reali.
- Avanzamento in `docs/fasi/`: un file per fase, più l'indice `README.md` con la sezione "Cosa fare adesso". Va aggiornato a ogni passo completato: spuntare le caselle, aggiornare lo stato e i prossimi passi, indicare chi fa cosa (🧑 l'utente, 🤖 Claude).

## Fasi
0 setup · 1 FEM di base (Lamé) · 2 CFD di base (Poiseuille, Womersley) · 3 segmentazione AI (AVT, Dice/HD95) · 4 geometria → mesh · 5 CFD su paziente reale · 6 FEM della parete · 7 surrogato AI.
