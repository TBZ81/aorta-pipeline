# Fase 7: modello AI surrogato (ampliamento)

**Obiettivo:** un modello AI che stima i risultati delle simulazioni (WSS, stress di parete) a partire dalla forma del vaso, in una frazione di secondo invece che in ore.
**Risultato misurabile:** R² e MAE rispetto alle simulazioni; quante volte è più veloce (*speed-up*).
**Stato:** ⏳ da iniziare.

## Passi previsti
- [ ] **20–40 geometrie:** famiglie parametriche di aneurismi idealizzati (FreeCAD) e/o varianti dei pazienti.
- [ ] **Simulazioni automatiche** su tutte le geometrie (gli script delle Fasi 5–6).
- [ ] **Descrittori della forma:** diametri, lunghezze, curvatura (dalla linea centrale).
- [ ] **Modello:** prima uno semplice (regressione, *gradient boosting*), poi eventualmente una rete piccola. Niente addestramento 3D pesante (Mac senza CUDA).
- [ ] **Validazione** su geometrie non viste in addestramento.

## Concetti da studiare
- Divisione addestramento/validazione/test e *overfitting*.
- R² e MAE.
- Quando un surrogato è affidabile e quando no (fuori dall'intervallo dei dati di addestramento).

## Strumenti
scikit-learn e PyTorch (`cardio-ai`), FreeCAD per le geometrie parametriche.
