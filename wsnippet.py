import fitz

doc = fitz.open("singlepage.pdf")
parola_cercata = "esercizi"

page = doc[0]

occurrences = page.search_for(parola_cercata)
if not occurrences:
    print("The word '{}' was not found on the page.".format(parola_cercata))
    doc.close()
    exit()

curr_page_width = page.rect.width
curr_page_number = page.number
i = 0
for occ in occurrences:
    i += 1
    line_margin = 3
    line_height = occ[3] - occ[1] + line_margin
    cropping = fitz.Rect(0, occ[1], curr_page_width, occ[1] + line_height * 2)

    doc.fullcopy_page(curr_page_number)
    cropped_page = doc[curr_page_number + i].set_cropbox(cropping)

doc.save("nuovofile.pdf")
doc.close()
