# Fase 4: dalla segmentazione alla mesh

**Obiettivo:** trasformare la segmentazione dell'aorta in una mesh di volume pronta per CFD e FEM.
**Risultato misurabile:** indici di qualità della mesh; numero di elementi compatibile con il Mac (circa 1M di tetraedri al massimo per la CFD).
**Stato:** ⏳ da iniziare. Il passaggio NIfTI → VMTK → `cardio` è già stato verificato il 28/10.

## Passi previsti
- [ ] **Superficie** dalla maschera (marching cubes in VMTK) e levigatura.
- [ ] **Linea centrale** con VMTK (ambiente `cardio-vmtk`, oppure in modo visivo con SlicerVMTK).
- [ ] **Taglio delle estremità** perpendicolare alla linea centrale e **prolungamenti** di ingresso e uscita (servono alla CFD).
- [ ] **Conversione da mm a m** (le immagini sono in mm, il codice usa i metri).
- [ ] **Mesh di volume** con gmsh: strati di elementi vicino alla parete (*boundary layer*) per il WSS.
- [ ] Creare `environment-vmtk.yml` per rendere riproducibile l'ambiente `cardio-vmtk`.

## Concetti da studiare
- Qualità degli elementi (rapporto d'aspetto, *skewness*).
- Perché servono i prolungamenti all'ingresso e all'uscita (flusso sviluppato, condizioni al contorno).
- Strato limite e risoluzione del WSS.

## Strumenti
VMTK (`cardio-vmtk`), 3D Slicer con SlicerVMTK, gmsh, ParaView.
