import fitz  # PyMuPDF
from PIL import Image


def insert_image(context):

    img = Image.open(context['image_path'])
    # Изменение размеров изображения не меняет их пропорций
    img_width, img_height = img.size


# Открываем существующий PDF
    pdf_path = context['file_name']
    doc = fitz.open(pdf_path)

    # Загружаем изображение
    image = open(context['image_path'], "rb").read()

    # Выбираем страницу (8-я страница имеет индекс 7)
    page = doc.load_page(context['page_num'])
    x, y = context['coordinates']

# Определяем позицию для вставки (200 px сверху и слева)
    rect = fitz.Rect(x, y, img_width * context['coef'] + x, img_height * context['coef'] + y)  # 100x100 - размеры изображения (можно подогнать под размеры картинки)

# Вставляем изображение
    page.insert_image(rect, stream=image)

# Сохраняем изменения в новый файл
    output_path = context['output_path']
    doc.save(output_path, incremental=context['incremental'], encryption=0)

# Закрываем документ
    doc.close()

context = {
    'image_path': 'page_8-image_4.png',
    'file_name': "Первичный анализ ниши пустая презентация.pdf",
    'page_num': 8,
    'coordinates': (160, 253),
    'coef': 0.62,
    'output_path': 'Первичный анализ ниши_с_картинкой.pdf',
    'incremental': False
}

insert_image(context)

context = {
    'image_path': 'page_10-image_3.png',
    'file_name': "Первичный анализ ниши_с_картинкой.pdf",
    'page_num': 10,
    'coordinates': (100, 253),
    'coef': 0.65,
    'output_path': 'Первичный анализ ниши_с_картинкой.pdf',
    'incremental': True
}

insert_image(context)
