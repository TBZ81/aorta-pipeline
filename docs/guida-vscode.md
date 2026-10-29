# Guida rapida: VS Code e terminale su Mac

Per chi parte da zero. Tastiera italiana: si usano solo scorciatoie che esistono davvero.

## 1. Aprire e chiudere il terminale

| Cosa vuoi fare | Come |
|---|---|
| **Mostrare o nascondere il terminale** | **`Cmd + J`** (la scorciatoia più importante) |
| Aprire un terminale nuovo | menu in alto **Terminal → New Terminal** |
| Se non trovi più niente | menu **View → Terminal** |

Il terminale sta **in basso**, nella scheda **TERMINAL**. Se vedi testo strano, controlla di essere su TERMINAL e non su PROBLEMS o OUTPUT.

⚠️ **Nascondere non è chiudere.** `Cmd + J` nasconde il pannello, ma il terminale resta vivo. Il **cestino** 🗑️ in alto a destra del pannello lo **chiude davvero**: dopo serve di nuovo `conda activate cardio`.

## 2. Leggere il prompt

```
(cardio) utente@computer aorta-pipeline %
```

| Pezzo | Significato |
|---|---|
| `(cardio)` | ambiente Python attivo. **Deve essere `cardio`** (o `cardio-ai` per l'AI). Se c'è `(base)`, scrivi `conda activate cardio` |
| `utente@computer` | si può ignorare |
| `aorta-pipeline` | cartella in cui ti trovi: deve essere questa |
| `%` | "sono pronto, scrivi". **Non va mai copiato** nel comando |

## 3. Sintassi dei comandi

Forma: **`programma  argomento  argomento`**, con le parole separate da **spazi**.

```bash
conda activate cardio                 # conda: attiva l'ambiente "cardio"
python scripts/fase1_a_mesh.py        # python: esegui questo file
pytest tests/test_fem_lame.py -v      # pytest: lancia i test (-v = dettagliato)
```

- **Un comando per volta**, poi **Invio**. Aspetta che ricompaia `%` prima di scriverne un altro.
- Maiuscole, minuscole e spazi contano.
- Dalle istruzioni copia **solo il contenuto del riquadro grigio**: niente `:`, niente `%`, niente testo intorno.
- Il testo dopo `#` è un commento: il terminale lo ignora.

## 4. Tasti utili nel terminale

| Tasto | Cosa fa |
|---|---|
| **`↑`** (freccia su) | richiama il comando precedente |
| **`Tab`** | completa i nomi di file e cartelle (`python scripts/fa` + Tab) |
| **`Ctrl + C`** (Ctrl, non Cmd!) | **ferma** un comando che non finisce |
| `Cmd + K` | pulisce lo schermo |
| `Cmd + C` / `Cmd + V` | copia e incolla |
| **`Cmd + clic`** su un percorso | apre quel file (ad esempio un'immagine `.png`) |

## 5. Gli errori più comuni

| Messaggio | Causa probabile | Soluzione |
|---|---|---|
| `command not found: ...` | refuso, oppure ambiente `(base)` | controlla cosa hai scritto, poi `conda activate cardio` |
| `No such file or directory` | cartella sbagliata, o nome del file sbagliato | `pwd` mostra la cartella; deve finire con `aorta-pipeline` |
| `ModuleNotFoundError` | ambiente sbagliato | `conda activate cardio` |

## 6. Altre scorciatoie di VS Code

| Tasto | Cosa fa |
|---|---|
| `Cmd + P` | apre un file scrivendone il nome |
| `Cmd + S` | salva il file (il pallino bianco sulla scheda indica che non è salvato) |
| `Cmd + Shift + V` | anteprima formattata dei file `.md` |
| `Cmd + B` | mostra o nasconde la barra dei file a sinistra |
| `Cmd + Z` | annulla l'ultima modifica |
| `Ctrl + Shift + G` | Source Control: commit e Sync con GitHub |
