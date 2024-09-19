import fitz  # PyMuPDF

# Открываем существующий PDF
pdf_path = "Первичный анализ ниши.pdf"
doc = fitz.open(pdf_path)

# Загружаем изображение
image_path = "page_8-image_4.png"
image = open(image_path, "rb").read()

# Выбираем страницу (8-я страница имеет индекс 7)
page = doc.load_page(8)

# Определяем позицию для вставки (200 px сверху и слева)
rect = fitz.Rect(100, 100, 100 + 904, 100 + 308)  # 100x100 - размеры изображения (можно подогнать под размеры картинки)

# Вставляем изображение
page.insert_image(rect, stream=image)

# Сохраняем изменения в новый файл
output_path = "Первичный анализ ниши_с_картинкой.pdf"
doc.save(output_path)

# Закрываем документ
doc.close()
