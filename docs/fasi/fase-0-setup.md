# Fase 0: setup

**Obiettivo:** un ambiente di lavoro completo e verificato sul Mac (M1 Pro, 16 GB), con il progetto su GitHub.
**Risultato misurabile:** gli script di verifica danno `ESITO: OK` e tutti i passaggi tra i programmi funzionano.
**Stato:** ✅ fatta. Restano 2 cose piccole (in fondo).

## Fatto
- [x] Miniforge e i tre ambienti conda:
  - `cardio`: FEniCSx, gmsh, OpenMPI, PyVista (FEM, CFD, mesh);
  - `cardio-ai`: PyTorch con la GPU Apple, TotalSegmentator (imaging e AI);
  - `cardio-vmtk`: VMTK, gira in Rosetta (linea centrale, Fase 4).
- [x] Struttura del progetto, `CLAUDE.md`, `README.md`, `.gitignore`.
- [x] Git con l'email anonima di GitHub; repository pubblico su github.com/TBZ81/aorta-pipeline.
- [x] Programmi: FreeCAD 1.1.4, ParaView 6.2.0, 3D Slicer 5.12.4.
- [x] Pacchetti per i grafici 3D nei notebook (trame, ipywidgets).
- [x] Verifica dei passaggi tra i programmi (28/10): FreeCAD → gmsh → FEniCSx → ParaView, superficie → VMTK, NIfTI → VMTK → `cardio`.

## Da fare
- [ ] 🧑 Aprire **3D Slicer** (la prima volta può impiegare 1–2 minuti, perché gira in Rosetta).
      Poi menu *View → Extensions Manager → Install Extensions* e installare **SlicerVMTK** e **SegmentEditorExtraEffects**, poi riavviare Slicer.
- [ ] 🧑 Quando Slicer funziona, svuotare il Cestino (contiene la vecchia versione 5.6.1, 1,4 GB).

## Comandi utili
```bash
conda activate cardio                    # attiva l'ambiente per FEM/CFD
python scripts/check_env_cardio.py       # verifica dell'ambiente
mpirun -n 4 python scripts/check_env_cardio.py   # la stessa, con 4 processi in parallelo
conda activate cardio-ai
python scripts/check_env_ai.py           # verifica dell'ambiente AI
```

## Cosa hai imparato
- **Ambiente conda:** una "scatola" con una versione precisa di Python e delle librerie. Ogni ambiente è separato dagli altri, così i pacchetti non vanno in conflitto.
- **Git:** il *commit* è una fotografia salvata del progetto, il *push* (o *Sync*) la manda su GitHub.
- **Rosetta:** traduce i programmi per processori Intel così che girino sul chip Apple. Funziona, ma è più lento.
