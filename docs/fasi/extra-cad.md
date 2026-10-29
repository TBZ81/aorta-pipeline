# Percorso parallelo: disegnare con FreeCAD

**Obiettivo:** imparare le basi del CAD 3D e produrre geometrie idealizzate che entrano nella pipeline.
**Quando:** nei momenti in cui hai voglia di qualcosa di più visivo, senza rallentare le fasi principali.
**Stato:** ⏳ da iniziare. FreeCAD 1.1.4 è installato; il passaggio FreeCAD → STEP → gmsh → FEniCSx è verificato.

## Esercizi
- [ ] **1 · Il tubo a parete spessa** (raggio interno 12,5 mm, parete 2 mm, lunghezza 50 mm), con gli stessi valori della Fase 1:
  workbench *Sketcher* (due cerchi con quote vincolate) → *Part Design* → *Pad* (estrusione) → esporta in STEP.
- [ ] **2 · Dal CAD al FEM:** il tuo STEP in gmsh e poi in FEniCSx per il Lamé in 3D (Fase 1, esercizio 8).
- [ ] **3 · Aneurisma fusiforme:** schizzo del profilo e *Revolution* attorno all'asse (serve nella Fase 6).
- [ ] **4 · Geometrie con parametri:** diametro e lunghezza dell'aneurisma da una tabella (*Spreadsheet*), per generare la famiglia di forme della Fase 7.
- [ ] **5 · (facoltativo) Stenosi e biforcazione** per la CFD (Fase 5).

## Concetti da studiare
- Schizzo vincolato: gradi di libertà, vincoli geometrici e quote.
- Operazioni solide: estrusione (*Pad*), rivoluzione, operazioni booleane.
- Formati di scambio: STEP (geometria esatta) e STL (triangoli).
- **Unità:** FreeCAD lavora in mm, il codice in metri (gmsh converte con `Geometry.OCCTargetUnit = "M"`).

## Risorse
Wiki ufficiale di FreeCAD, tutorial **"Basic Part Design Tutorial"**.
