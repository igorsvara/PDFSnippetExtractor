import fitz

doc = fitz.open("DB_2023-01-27.pdf")
new_doc_name = "nuovofile.pdf"
snippet_line_number = 2
parola_cercata = "base di dati"


doc_page_number = doc.page_count
relative_shift = 0
for x in range(doc_page_number):
    page = doc[x + relative_shift]

    curr_page_number = page.number
    curr_page_width = page.rect.width
    curr_page_height = page.rect.height

    occurrences = page.search_for(parola_cercata)
    if not occurrences:
        continue

    i = 0
    for occ in occurrences:
        line_margin = 3
        line_height = occ[3] - occ[1] + line_margin
        y_end_crop = occ[1] + line_height * snippet_line_number
        if y_end_crop > curr_page_height:
            y_end_crop = curr_page_height
        cropping = fitz.Rect(0, occ[1], curr_page_width, y_end_crop)

        # Inserisco la copia subito dopo alla posizione indicata con curr_page_number  + i
        doc.fullcopy_page(curr_page_number, curr_page_number + i)
        # Ritaglio la pagina appena inserita
        print(f"{curr_page_number+i+1} page -> crop {cropping}")
        doc[curr_page_number + i + 1].set_cropbox(cropping)
        i += 1

    relative_shift += i
    # doc.delete_page(curr_page_number)

doc.save(new_doc_name)
doc.close()
