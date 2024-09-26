import fitz  # PyMuPDF
from PIL import Image

def insert_images(contexts):

    def insert_repeated_image(page, image, rect, repeat_count=1, interval=0, direction='horizontal_asc'):
    # Вставляем картинку несколько раз с интервалом
        for i in range(repeat_count):
            if direction == 'horizontal_asc':
                offset_rect = rect + (i * interval, 0, i * interval, 0)
            elif direction == 'horizontal_desc':
                offset_rect = rect - (i * interval, 0, i * interval, 0)
            else:
                offset_rect = rect + (0, i * interval, 0, i * interval)
            page.insert_image(offset_rect, stream=image)

    # Открываем существующий PDF
    doc = fitz.open(contexts[0]['file_name'])
    incremental = contexts[0]['incremental']
    output_path = contexts[0]['output_path']

    for index, context in enumerate(contexts):
        # Если incremental текущего контекста отличается от предыдущего, сохраняем файл, прежде, чем продолжить
        if not context['incremental'] == incremental or not context['output_path'] == output_path:
            doc.save(contexts[index - 1]['output_path'], incremental=contexts[index - 1]['incremental'], encryption=0)
            doc.close()
            incremental = contexts[index]['incremental']
            output_path = contexts[index]['output_path']
            doc = fitz.open(contexts[index]['file_name'])

        img = Image.open(context['image_path'])
        img_width, img_height = img.size
        # Загружаем изображение
        image = open(context['image_path'], "rb").read()
        # Выбираем страницу
        page = doc.load_page(context['page_num'])
        x, y = context['coordinates']
        # Определяем позицию для вставки
        rect = fitz.Rect(x, y, img_width * context['coef'] + x, img_height * context['coef'] + y)
        # Определяем количество раз, которые нужно выполнить вставку изображения
        repeat_insertion = context.get('repeat_insertion', False)
        if repeat_insertion:
            repeat_count = repeat_insertion.get('repeat_count', 1)
            interval = repeat_insertion.get('interval', 0)
            direction = repeat_insertion.get('direction', 'horizontal')
            # Вставляем изображение
            insert_repeated_image(page, image, rect, repeat_count, interval, direction)
        else:
            insert_repeated_image(page, image, rect)

    # Сохраняем изменения один раз в конце
    doc.save(output_path, incremental=incremental, encryption=0)
    # Закрываем документ
    doc.close()

contexts = [
    {
        'image_path': 'page_8-image_4.png',
        'file_name': "без данных.pdf",
        'page_num': 8,
        'coordinates': (160, 253),
        'coef': 0.62,
        'output_path': 'Первичный анализ ниши_с_картинкой.pdf',
        'incremental': False
    },
    {
        'image_path': 'page_10-image_3.png',
        'file_name': "Первичный анализ ниши_с_картинкой.pdf",
        'page_num': 10,
        'coordinates': (100, 253),
        'coef': 0.65,
        'output_path': 'Первичный анализ ниши_с_картинкой.pdf',
        'incremental': True
    }
]

insert_images(contexts)
