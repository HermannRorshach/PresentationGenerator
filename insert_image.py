import fitz  # PyMuPDF
from PIL import Image

img = Image.open("page_8-image_4.png")
img_width, img_height = img.size


# Открываем существующий PDF
pdf_path = "Первичный анализ ниши пустая презентация.pdf"
doc = fitz.open(pdf_path)

# Загружаем изображение
image_path = "page_8-image_4.png"
image = open(image_path, "rb").read()

# Выбираем страницу (8-я страница имеет индекс 7)
page = doc.load_page(8)
x = 160
y = 253
# Определяем позицию для вставки (200 px сверху и слева)
rect = fitz.Rect(x, y, img_width * 0.62 + x, img_height * 0.62 + y)  # 100x100 - размеры изображения (можно подогнать под размеры картинки)

# Вставляем изображение
page.insert_image(rect, stream=image)

# Сохраняем изменения в новый файл
output_path = "Первичный анализ ниши_с_картинкой.pdf"
doc.save(output_path)

# Закрываем документ
doc.close()
