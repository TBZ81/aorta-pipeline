# Fase 5: CFD su paziente reale

**Obiettivo:** simulare il flusso sanguigno pulsatile nell'aorta di un paziente reale.
**Risultato misurabile:** pressione fisiologica (circa 120/80 mmHg), mappe di TAWSS e OSI, risultati che cambiano meno del 5% raffinando la mesh.
**Stato:** ⏳ da iniziare.

## Passi previsti
- [ ] **Flusso in ingresso** dalla letteratura (forma d'onda aortica nel ciclo cardiaco).
- [ ] **Uscite con modello Windkessel RCR** (resistenze e capacità che rappresentano la circolazione a valle).
- [ ] **Simulazione pulsatile** in parallelo (`mpirun -n 4`) su più cicli, fino a regime.
- [ ] **TAWSS, OSI e pressione** sulla parete; visualizzazione e animazioni in ParaView.
- [ ] **Studio di indipendenza dalla mesh** (almeno due mesh).
- [ ] (Facoltativo) primo caso su una geometria idealizzata disegnata in FreeCAD, per esempio una stenosi.

## Concetti da studiare
- Modello Windkessel a 3 elementi (RCR) e come si tara.
- TAWSS (WSS mediato nel tempo) e OSI.
- Limiti: parete rigida, sangue newtoniano. Vanno scritti nel README.

## Strumenti
FEniCSx con MPI, ParaView. Mesh dalla Fase 4.
