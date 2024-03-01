import os
import re
import fitz

'''
Usage:
- Modifica `from_pdf` per specificare il percorso del PDF da cui estrarre gli snippets.
- Modifica `s_pattern` per cambiare il pattern regex di ricerca.
- Modifica `snippet_line_number` per modificare l'altezza dello snippet estratto.
- Modifica `line_margin` per modificare il margine tra le righe dello snippet estratto.
'''
from_pdf = "pdf_src/dispenseLM2122.pdf"
s_pattern = re.compile("(Teorema|Definizione|Algoritmo|Convenzione|Corollario)\s\d+\.\d+(\.)?")
snippet_line_number = 6
line_margin = 3

# Preparazione del nuovo documento
new_doc_name = f"results/{os.path.basename(from_pdf)[:-4]}-result.pdf"
doc = fitz.open(from_pdf)
new_doc = fitz.open()

# Iterazione attraverso le pagine del documento originale
y = 0
for page in doc:
    # Estrai le informazioni generali sulla pagina corrente
    curr_page_number = page.number
    curr_page_width = page.rect.width
    curr_page_height = page.rect.height

    # Trova tutte le occorrenze del pattern nella pagina
    p_iterator = s_pattern.findall(page.get_text())

    # Lista per salvare le occorrenze esatte (case-sensitive)
    occurrences = []

    # Utilizza finditer() per cercare tutte le occorrenze
    for match in s_pattern.finditer(page.get_text()):
        # La funzione search_for è case-insensitive, ricerca tutte le occorrenze
        insensitive_match = page.search_for(match.group(0))

        # Salva solo le occorrenze esattamente uguali al match originale (case-sensitive)
        for ins in insensitive_match:
            if page.get_textbox(ins) == match.group(0):
                occurrences.append(ins)

    # Se non ci sono occorrenze, passa alla prossima pagina
    if not occurrences:
        continue

    # Itera attraverso le occorrenze trovate
    for i, occ in enumerate(occurrences):
        # Determina il rettangolo da ritagliare dalla pagina corrente
        line_height = occ[3] - occ[1] + line_margin
        y_end_crop = occ[1] + line_height * snippet_line_number
        if y_end_crop > curr_page_height:
            y_end_crop = curr_page_height
        cropping = fitz.Rect(0, occ[1], curr_page_width, y_end_crop)

        # Inserisci una copia della pagina corrente nel nuovo documento
        new_doc.insert_pdf(doc, from_page=curr_page_number, to_page=curr_page_number)

        # Ritaglia la pagina appena inserita
        new_doc[y].set_cropbox(cropping)

        # Incrementa l'indice y ogni volta che viene inserita una nuova pagina nel nuovo PDF
        y += 1

        # Stampo le parole trovate con la relativa pagina
        print(f"page: {page.number} -> match: {page.get_textbox(occ)}")

# Salva il nuovo documento se contiene almeno una pagina
if new_doc.page_count:
    new_doc.save(new_doc_name)

# Chiude entrambi i documenti
new_doc.close()
doc.close()