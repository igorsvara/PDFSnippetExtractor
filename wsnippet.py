import fitz

doc = fitz.open("dispenseLM2122.pdf")
page = doc[11]

parola_cercata = "utilizza"

new_doc = fitz.open()
# new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)

# # Recupera le coordinate del rettangolo della parola trovata
# for occ in page.search_for(parola_cercata):
#     t_page = page
#     cropping = fitz.Rect(occ[:4])
#     cropped_page = t_page.set_cropbox(cropping)
#     new_doc.insert_pdf(cropped_page)

occurrences = page.search_for(parola_cercata)
if not occurrences:
    print("The word '{}' was not found on the page.".format(parola_cercata))
    new_doc.close()
    doc.close()
    exit()

# Extract the coordinates of the first occurrence
first_occ = occurrences[0]
t_page = page

cropping = fitz.Rect(first_occ[:4])
t_page.set_cropbox(cropping)
# t_page.set_cropbox(t_page.mediabox)

t_page.show_pdf_page(cropping, fitz.open("dispenseLM2122.pdf"))

#
# new_doc.insert_page(0,t_page)
# new_doc.save("nuovofile.pdf")
doc.close()
new_doc.close()



"""
import fitz

doc = fitz.open("dispenseLM2122.pdf")
page = doc[11]

parola_cercata = "utilizza"
rect = page.search_for(parola_cercata)[0]

# Estrai la parte del PDF definita dal rettangolo
new_page_content = page.get_rect(rect)

# Creare un nuovo documento PDF
new_doc = fitz.open()

# Aggiungere una nuova pagina al nuovo documento
new_page = new_doc.new_page(width=rect[2] - rect[0], height=rect[3] - rect[1])

# Inserire la parte del PDF nella nuova pagina
new_page.insert_text((0, 0), new_page_content)

# Salvare il nuovo documento come PDF
new_doc.save("nuovo_cropped_file.pdf")
new_doc.close()
"""