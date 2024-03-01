# Estrazione Snippets da PDF

Questo script Python utilizza la libreria PyMuPDF (MuPDF) per estrarre snippets da un documento PDF basandosi su un pattern regex. Gli snippets estratti vengono poi salvati in un nuovo documento PDF.

## Istruzioni d'uso

1. Modifica `from_pdf` nel codice per specificare il percorso del PDF da cui estrarre gli snippets.
2. Modifica `s_pattern` per cambiare il pattern regex di ricerca.
3. Modifica `snippet_line_number` per regolare l'altezza dello snippet estratto.
4. Modifica `line_margin` per regolare il margine tra le righe dello snippet estratto.

Esegui lo script Python. Il nuovo documento PDF contenente gli snippets estratti sarà salvato nella cartella "results".

## Dipendenze

Assicurati di avere le seguenti librerie Python installate:

```bash
pip install PyMuPDF
```

## Esempio

```bash
python extract_snippets.py
```


---
Autore: Igor Svara