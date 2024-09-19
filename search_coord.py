import fitz  # PyMuPDF

# Открываем PDF файл
pdf_path = "Первичный анализ ниши.pdf"
doc = fitz.open(pdf_path)

# Указываем слово для поиска
search_word = "5643"

# Выбираем страницу для поиска (например, 8-я страница, индекс 7)
page = doc.load_page(9)

# Находим все вхождения слова на странице
text_instances = page.search_for(search_word)

# Выводим координаты каждого найденного вхождения
for instance in text_instances:
    print(f"Найдено слово '{search_word}' с координатами: {instance}")

# Закрываем документ
doc.close()
