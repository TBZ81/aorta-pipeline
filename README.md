# aorta-pipeline

Pipeline open source per la biomeccanica dell'aorta paziente-specifica:
**imaging → segmentazione AI → mesh → CFD + FEM → modello surrogato AI**.

> 🚧 Work in progress — il README verrà completato fase per fase con risultati e figure.

## Stato

| Fase | Contenuto | Stato |
|---|---|---|
| 0 | Setup ambiente e verifica | ✅ |
| 1 | FEM di base: cilindro a parete spessa vs soluzione analitica di Lamé | ⏳ |
| 2 | CFD di base: Poiseuille e Womersley vs soluzione analitica | ⏳ |
| 3 | Segmentazione AI dell'aorta (TotalSegmentator vs segmentazione manuale) | ⏳ |
| 4 | Dalla segmentazione alla mesh | ⏳ |
| 5 | CFD pulsatile su paziente reale (WSS, OSI, pressione) | ⏳ |
| 6 | FEM della parete iperelastica (stress di picco) | ⏳ |
| 7 | Modello surrogato AI | ⏳ |

## Installazione

Richiede [Miniforge](https://github.com/conda-forge/miniforge).

```bash
mamba env create -f environment.yml      # FEM / CFD
mamba env create -f environment-ai.yml   # imaging / AI

conda activate cardio
mpirun -n 4 python scripts/check_env_cardio.py

conda activate cardio-ai
python scripts/check_env_ai.py
```

Testato su macOS (Apple M1 Pro, 16 GB RAM).
