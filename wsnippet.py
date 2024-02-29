import os, fitz

from_pdf = "pdf_src/<your_pdf>.pdf"
parola_cercata = "Definizione"

new_doc_name = f"results/{os.path.basename(from_pdf)[:-4]}-result.pdf"
snippet_line_number = 6
line_margin = 3

doc = fitz.open(from_pdf)
new_doc = fitz.open()

# y e' indice delle pagine all'interno del nuovo file
y = 0
for x in range(doc.page_count):
    page = doc[x]

    curr_page_number = page.number
    curr_page_width = page.rect.width
    curr_page_height = page.rect.height

    occurrences = page.search_for(parola_cercata)
    if not occurrences:
        continue

    for i, occ in enumerate(occurrences):
        line_height = occ[3] - occ[1] + line_margin
        y_end_crop = occ[1] + line_height * snippet_line_number
        if y_end_crop > curr_page_height:
            y_end_crop = curr_page_height
        cropping = fitz.Rect(0, occ[1], curr_page_width, y_end_crop)

        new_doc.insert_pdf(doc, from_page=curr_page_number, to_page=curr_page_number)
        new_doc[y].set_cropbox(cropping)
        # incremento y ogni volta che inserisco una pagina nel nuovo pdf
        y += 1

if new_doc.page_count:
    new_doc.save(new_doc_name)
new_doc.close()
doc.close()
