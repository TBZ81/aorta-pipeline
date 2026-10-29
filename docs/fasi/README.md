# Fasi del progetto: indice

Un file per fase: obiettivo, risultato misurabile, cosa fare (spuntato quando è fatto), concetti da studiare.
Claude li aggiorna man mano che si procede.

**Come leggerli in VS Code:** apri un file e premi `Cmd+Shift+V` per l'anteprima formattata.

**Chi fa cosa:**
- 🧑 **tu**: comandi da eseguire, codice da scrivere, programmi da usare;
- 🤖 **Claude**: prepara struttura, test e codice di contorno; controlla e spiega.

| Fase | Contenuto | Stato |
|---|---|---|
| [0](fase-0-setup.md) | Setup: ambienti, strumenti, GitHub | ✅ fatta (restano 2 cose piccole) |
| [1](fase-1-fem-lame.md) | FEM di base: cilindro di Lamé | 🔄 **in corso: esercizio 3 fatto, ora il commit** |
| [2](fase-2-cfd-base.md) | CFD di base: Poiseuille e Womersley | ⏳ |
| [3](fase-3-segmentazione.md) | Segmentazione AI dell'aorta | ⏳ |
| [4](fase-4-geometria-mesh.md) | Dalla segmentazione alla mesh | ⏳ |
| [5](fase-5-cfd-paziente.md) | CFD su paziente reale | ⏳ |
| [6](fase-6-fem-parete.md) | FEM della parete iperelastica | ⏳ |
| [7](fase-7-surrogato-ai.md) | Modello AI surrogato | ⏳ |
| [CAD](extra-cad.md) | Percorso parallelo: disegnare con FreeCAD | ⏳ |

## 👉 Cosa fare adesso
1. 🧑 Commit e Sync della [Fase 1](fase-1-fem-lame.md), messaggio `Fase 1: solutore FEM per il cilindro di Lamé`.
2. 🤖 + 🧑 Esercizio 4: risultati in XDMF e visualizzazione in ParaView.
3. 🧑 Aprire 3D Slicer e installare le estensioni SlicerVMTK e SegmentEditorExtraEffects ([Fase 0](fase-0-setup.md)).
