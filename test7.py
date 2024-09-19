import fitz  # pymupdf

# Открытие существующего PDF-файла
pdf_document = fitz.open('Первичный анализ ниши.pdf')

# Выбор страницы, на которой нужно работать
page = pdf_document.load_page(0)  # Первая страница (индекс 0)

# Извлечение изображений из страницы
image_list = page.get_images(full=True)
if not image_list:
    raise ValueError("No images found on the page")

# Выведем список изображений для проверки
print("Image List:", image_list)

# Получение изображений
xref1 = image_list[0][0]  # xref изображения
xref2 = image_list[2][0]
base_image1 = pdf_document.extract_image(xref1)
image_bytes1 = base_image1["image"]
base_image2 = pdf_document.extract_image(xref2)
image_bytes2 = base_image2["image"]

# Создание pixmap для получения размера изображения
pix1 = fitz.Pixmap(pdf_document, xref1)
pix2 = fitz.Pixmap(pdf_document, xref2)

# Создание прямоугольника для изображения на основе размеров pixmap
image_rect1 = fitz.Rect(0, 0, pix1.width * 1.2, pix1.height * 1.2)
image_rect2 = fitz.Rect(200, 200, pix2.width*1.2, pix2.height*1.2)

# Вставка изображения на страницу
page.insert_image(
    image_rect1,  # Положение и размер изображения
    stream=image_bytes1,
    overlay=True
)

page.insert_image(
    image_rect2,  # Положение и размер изображения
    stream=image_bytes2,
    overlay=True
)


# Добавление нового текста поверх изображения
text = "Huyak! Яблоко-малина!"
text_position = (100, 100)  # Позиция (x, y) для текста
font_path = 'Montserrat-SemiBold.ttf'
fontname = 'CustomFont'

# Вставка кастомного шрифта
page.insert_font(fontfile=font_path, fontname=fontname)

# Добавление текста
page.insert_text(
    text_position,              # Позиция текста
    text,                       # Содержимое текста
    fontsize=90,                # Размер шрифта
    fontname=fontname,          # Имя кастомного шрифта
    color=(1, 0, 0)             # Цвет текста (в диапазоне от 0 до 1)
)

# Сохранение изменений в новый PDF-файл
pdf_document.save('output.pdf')
pdf_document.close()
