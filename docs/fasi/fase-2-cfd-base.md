# Fase 2: CFD di base, Poiseuille e Womersley

**Obiettivo:** verificare il solutore CFD (Navier-Stokes in FEniCSx) su flussi in un tubo con soluzione esatta, prima di usarlo sull'aorta.
**Risultato misurabile:** errore rispetto alla soluzione analitica e curva di convergenza; WSS calcolato confrontato con quello teorico.
**Stato:** ⏳ da iniziare.

## Passi previsti
- [ ] **Poiseuille 2D e 3D** (flusso stazionario): profilo parabolico, caduta di pressione, WSS = 4μQ/(πR³).
- [ ] **Womersley** (flusso pulsatile): profilo di velocità con le funzioni di Bessel; numero di Womersley α circa 10–20 nell'aorta.
- [ ] **Schema temporale** e stabilità: passo temporale, numero di Courant.
- [ ] **Calcolo di WSS e OSI** sul tubo: gli stessi indici che useremo sul paziente.
- [ ] Notebook della fase e grafici per il README.

## Concetti da studiare
- Equazioni di Navier-Stokes incomprimibili; il sangue come fluido newtoniano (μ ≈ 3,5 mPa·s, ρ ≈ 1060 kg/m³).
- Elementi stabili per velocità e pressione (Taylor-Hood P2-P1).
- Numero di Reynolds e di Womersley.
- WSS (wall shear stress) e OSI (oscillatory shear index): cosa misurano e perché contano per l'aterosclerosi e gli aneurismi.

## Strumenti
FEniCSx (ambiente `cardio`), ParaView per i campi di velocità, notebook per i grafici.
