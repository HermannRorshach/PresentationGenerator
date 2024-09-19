import pymupdf



doc = pymupdf.open('Первичный анализ ниши.pdf')
print(len(doc))
for page in doc[2:]:
    # links = page.get_links()
    # for link in links:
    #     print(link['uri'])
    # pix = page.get_pixmap()
    # pix.save("page-%i.png" % page.number)
    areas = page.search_for("капитализация")
    print(areas)
    break

doc.select([1, 2])



doc.save('output.pdf')
doc.close()



# Пример использования
# replace_text_in_pdf('Первичный анализ ниши.pdf', 'text_change.pdf', 'Avito', 'Huito!')
