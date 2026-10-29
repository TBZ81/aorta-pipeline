# Fase 6: FEM della parete iperelastica

**Obiettivo:** calcolare lo stress nella parete aortica con un materiale iperelastico, come nella valutazione del rischio di rottura degli aneurismi.
**Risultato misurabile:** stress di picco a pressione sistolica, confrontato con i valori pubblicati in letteratura.
**Stato:** ⏳ da iniziare. Si basa sull'esercizio iperelastico della Fase 1.

## Passi previsti
- [ ] **Modello di Raghavan–Vorp** (iperelastico isotropo per la parete degli aneurismi aortici addominali).
- [ ] **Geometria idealizzata** prima: aneurisma fusiforme disegnato in FreeCAD.
- [ ] **Geometria del paziente:** parete con spessore uniforme ricavata dalla superficie del lume.
- [ ] **Carico:** pressione sistolica; soluzione non lineare con metodo di Newton e incrementi di carico.
- [ ] **Stress di picco** (von Mises, principale massimo) e confronto con la letteratura.
- [ ] (Facoltativo) confronto con CalculiX dentro FreeCAD.

## Concetti da studiare
- Iperelasticità: energia di deformazione, grandi deformazioni, tensori F, C, S.
- Modello di Raghavan–Vorp e i suoi parametri.
- Metodo di Newton e incremento del carico.
- Limiti: spessore uniforme, nessuna tensione residua, materiale isotropo.

## Strumenti
FEniCSx, FreeCAD (geometrie idealizzate), ParaView.
