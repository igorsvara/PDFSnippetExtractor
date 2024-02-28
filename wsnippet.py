import fitz

doc = fitz.open("singlepage.pdf")
parola_cercata = "formula"

page = doc[0]

occurrences = page.search_for(parola_cercata)
if not occurrences:
    print("The word '{}' was not found on the page.".format(parola_cercata))
    doc.close()
    exit()

# for occ in occurrences:
#     cropping = fitz.Rect(occ[:4])
#     cropped_page = t_page.set_cropbox(cropping)
#     new_doc.insert_pdf(cropped_page)

doc.new_page(page)


# first_occ = occurrences[0]
# line_margin = 3
# line_height = first_occ[3] - first_occ[1] + line_margin
#
# cropping = fitz.Rect(0, first_occ[1], page.rect.width, first_occ[1] + line_height * 5)
# page.set_cropbox(cropping)


doc.save("nuovofile.pdf")
doc.close()