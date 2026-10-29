# Fase 3: segmentazione AI dell'aorta

**Obiettivo:** ottenere l'aorta dalle TC con un modello AI preaddestrato e misurare quanto è accurato rispetto alla segmentazione manuale degli esperti.
**Risultato misurabile:** Dice, HD95 (distanza di Hausdorff al 95%) e differenza dei diametri massimi in mm.
**Stato:** ⏳ da iniziare.

## Passi previsti
- [ ] **Dataset AVT** (Aortic Vessel Tree, Radl et al. 2022, figshare): script di download in `scripts/`, solo un sottoinsieme di casi, licenza citata nel README.
- [ ] **TotalSegmentator** (ambiente `cardio-ai`, con la GPU Apple) sulle TC del dataset.
- [ ] **Metriche:** Dice, HD95 e diametro massimo, confrontati con le segmentazioni manuali.
- [ ] **Controllo visivo in 3D Slicer:** TC e segmentazione sovrapposte, ritocchi con il Segment Editor.
- [ ] Tabella dei risultati e figure per il README.

## Concetti da studiare
- Formato NIfTI e DICOM; *spacing* dei voxel (in mm).
- Rete U-Net e nnU-Net (la base di TotalSegmentator): cosa fa, senza addestrarla.
- Dice e HD95: cosa misurano e perché servono entrambe.

## Strumenti
TotalSegmentator e PyTorch (`cardio-ai`), 3D Slicer 5.12.4.
