from PIL import Image
import fitz
from insert_images import insert_images
from insert_text import insert_texts


context_scale_value = {
    'file_name': 'output.pdf',
    'page_num': 7,
    'font_size': 30,
    'font_path': 'Code-Pro-Bold-LC.ttf',
    'text': '0',
    'color': (1, 1, 1),
    'y_coordinate': 700,
    'x_center': 370,  # Центр текста по оси X
    'text_width': 180,  # Ширина текстового блока
    'margin': 10,
    'output_path': 'output.pdf',
    'incremental': True
    }

context_insert_images = [
    {
        'image_path': 'Line 1.png',
        'file_name': 'output.pdf',
        'page_num': 7,
        'coordinates': (1114, 283),
        'repeat_insertion': {
            'repeat_count': 5,
            'interval': 186,
            'direction': 'horizontal_desc'
            },
        'coef': 1,
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'image_path': 'output_image_1.png',
        'file_name': 'output.pdf',
        'page_num': 7,
        'coordinates': (376, 350),
        'coef': 1,
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'image_path': 'output_image_2.png',
        'file_name': 'output.pdf',
        'page_num': 7,
        'coordinates': (376, 517),
        'coef': 1,
        'output_path': 'output.pdf',
        'incremental': True
    }
]

contexts_for_values_in_side = [
    {
        'file_name': 'output.pdf',
        'page_num': 7,
        'font_size': 30,
        'font_path': 'Code-Pro-Bold-LC.ttf',
        'text': '5643',
        'color': (1, 1, 1),
        'coordinates': [390, 390],
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 7,
        'font_size': 30,
        'font_path': 'Code-Pro-Bold-LC.ttf',
        'text': '5643',
        'color': (1, 1, 1),
        'coordinates': [390, 560],
        'output_path': 'output.pdf',
        'incremental': True
    }
]

context_values_in_rectangles = [
    {
    'file_name': 'output.pdf',
    'page_num': 7,
    'font_size': 30,
    'font_path': 'Code-Pro-Bold-LC.ttf',
    'text': '0',
    'color': (0, 0, 0),
    'y_coordinate': 367,
    'x_center': 500,  # Центр текста по оси X
    'text_width': 180,  # Ширина текстового блока
    'margin': 10,
    'output_path': 'output.pdf',
    'incremental': True
    }
]

def add_centered_text(contexts):
    # Открываем существующий PDF
    doc = fitz.open(contexts[0]['file_name'])

    for context in contexts:

        # Загружаем первую страницу для редактирования
        page = doc.load_page(context['page_num'])
        font_path = context['font_path']

        # Вставка кастомного шрифта на страницу
        fontname = 'CustomFont'
        page.insert_font(fontfile=font_path, fontname=fontname)

        # Параметры страницы и текста
        current_y = context['y_coordinate']
        text_x_center = context['x_center']
        text_width = context['text_width']
        margin = context['margin']

        # Прямоугольник для вставки текста с выравниванием по заданной координате X
        left_x = text_x_center - (text_width / 2)
        right_x = text_x_center + (text_width / 2)
        text_rect = fitz.Rect(left_x, current_y, right_x, current_y + context['font_size'] * 10)

        # Вставляем текст с кастомным шрифтом
        page.insert_textbox(text_rect, context['text'], fontsize=context['font_size'], fontname='CustomFont', fill=context['color'], align=1)

    # Сохраняем изменения в новый файл
    doc.save(context['output_path'], incremental=True, encryption=0)
    doc.close()

coordinates_numbers_on_scale = (370, 556, 742, 928)

def calculate_scale_and_widths(value_1, value_2):
    max_value = max(value_1, value_2)

    step = 1
    max_scale_value = step * 5
    level = 0

    while max_scale_value < max_value:
        level += 1
        step = max_scale_value
        if (level % 3 == 0) or (level % 3 == 2):
            max_scale_value = step * 5
        elif level % 3 == 1:
            max_scale_value = step * 4

    img_1_width = int(value_1 / (step / 186))
    img_2_width = int(value_2 / (step / 186))

    scale_marks = [step * _ for _ in range(5)]

    return img_1_width, img_2_width, scale_marks

def is_text_fitting(value, font_path, img_width, context):
    font = fitz.Font(fontfile=font_path)
    # Вычисляем ширину текста в точках
    text_width_actual = font.text_length(str(value), fontsize=context['font_size'])

    # Проверяем, поместится ли текст в указанный прямоугольник
    if text_width_actual > img_width:
        return False
    return True

def add_transparent_gap_to_line(input_image_path, output_image_path, gap_start, gap_height):
    # Открываем исходное изображение
    image = Image.open(input_image_path).convert("RGBA")

    # Получаем размеры исходного изображения
    width, height = image.size

    # Создаем новое изображение с таким же размером и поддержкой прозрачности
    new_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Копируем часть изображения до разрыва
    new_image.paste(image.crop((0, 0, width, gap_start)), (0, 0))

    # Копируем часть изображения после разрыва
    new_image.paste(image.crop((0, gap_start + gap_height, width, height)), (0, gap_start + gap_height))

    # Сохраняем новое изображение
    new_image.save(output_image_path, "PNG")

def handle_text_overflow(value_1, value_2, img_1_width, img_2_width, context):
    flag_1, flag_1_1, flag_2 = False, False, False
    interval = context_insert_images[0]['repeat_insertion']['interval']
    if (not is_text_fitting(value_1, 'Code-Pro-LC.ttf', img_1_width, context) and not is_text_fitting(value_1, 'Code-Pro-LC.ttf', abs(interval - img_1_width), context)) or (not is_text_fitting(value_2, 'Code-Pro-LC.ttf', img_2_width, context) and not is_text_fitting(value_2, 'Code-Pro-LC.ttf', abs(interval - img_2_width), context)):
        context_insert_images[0]['repeat_insertion']['repeat_count'] = 3
        print('Уменьшили количество линий')
    if not is_text_fitting(value_1, 'Code-Pro-LC.ttf', img_1_width, context):
        flag_1 = True
        if not is_text_fitting(value_1, 'Code-Pro-LC.ttf', abs(interval - img_1_width), context):
            input_image_path = 'Line 1.png'
            output_image_path = 'line_with_gap.png'
            gap_start = 67  # Начало разрыва (в пикселях)
            gap_height = 60  # Высота разрыва (в пикселях)
            flag_1_1 = True
            add_transparent_gap_to_line(input_image_path, output_image_path, gap_start, gap_height)
        contexts_for_values_in_side[0]['coordinates'][0] = 376 + img_1_width + 30
        contexts_for_values_in_side[0]['text'] = str(value_1)
        insert_texts([contexts_for_values_in_side[0]])

    if not is_text_fitting(value_2, 'Code-Pro-LC.ttf', img_2_width, context):
        flag_2 = True
        if not is_text_fitting(value_2, 'Code-Pro-LC.ttf', abs(interval - img_2_width), context):
            if flag_1_1:
                input_image_path = 'line_with_gap.png'
            else:
                input_image_path = 'Line 1.png'
            output_image_path = 'line_with_gap.png'
            gap_start = 234  # Начало разрыва (в пикселях)
            gap_height = 60  # Высота разрыва (в пикселях)

            add_transparent_gap_to_line(input_image_path, output_image_path, gap_start, gap_height)

        contexts_for_values_in_side[1]['coordinates'][0] = 376 + img_2_width + 30
        contexts_for_values_in_side[1]['text'] = str(value_2)
        insert_texts([contexts_for_values_in_side[1]])

    context_lines = [
        {
            'image_path': 'Line 1.png',
            'file_name': 'output.pdf',
            'page_num': 7,
            'coordinates': (370, 283),
            'coef': 1,
            'output_path': 'output.pdf',
            'incremental': True
        },
        {
            'image_path': 'line_with_gap.png',
            'file_name': 'output.pdf',
            'page_num': 7,
            'coordinates': (556, 283),
            'coef': 1,
            'output_path': 'output.pdf',
            'incremental': True
        }
        ]

    context_lines.extend(context_insert_images)
    insert_images(context_lines)

    return flag_1, flag_2


def create_diagram_page_8(context):
    value_1 = context['value_1']
    value_2 = context['value_2']

    img_1_width, img_2_width, scale_marks = calculate_scale_and_widths(value_1, value_2)

    img_height = 60

    # Цвет (в формате RGB)
    color_1 = (255, 255, 255)  # Цвет B8FF00 в формате RGB
    color_2 = (184, 255, 0)

    # Создание нового изображения
    image_1 = Image.new("RGB", (img_1_width, img_height), color_1)
    image_2 = Image.new("RGB", (img_2_width, img_height), color_2)

    # Сохранение изображения в формате PNG
    image_1.save("output_image_1.png")
    image_1.close()

    image_2.save("output_image_2.png")
    image_2.close()

    context_values_in_rectangles[0]['x_center'] = 370 + img_1_width / 2
    context_values_in_rectangles[0]['text'] = str(value_1)
    copy = {key: value for key, value in context_values_in_rectangles[0].items()}
    copy['x_center'] = 370 + img_2_width / 2
    copy['text'] = str(value_2)
    copy['y_coordinate'] = 536
    context_values_in_rectangles.append(copy)

    if (is_text_fitting(value_1, 'Code-Pro-LC.ttf', img_1_width, context) and is_text_fitting(value_2, 'Code-Pro-LC.ttf', img_2_width, context)):
        insert_images(context_insert_images)
        add_centered_text(context_values_in_rectangles)
    else:
        flag_1, flag_2 = handle_text_overflow(value_1, value_2, img_1_width, img_2_width, context)
        if not flag_1:
            add_centered_text([context_values_in_rectangles[0]])
        if not flag_2:
            add_centered_text([context_values_in_rectangles[1]])



    context_text = []
    x_center = context_scale_value['x_center']
    for mark in scale_marks:
        copy = {key: value for key, value in context_scale_value.items()}
        copy['text'] = str(mark)
        copy['x_center'] = x_center
        context_text.append(copy)
        x_center += 186
    add_centered_text(context_text)

context = {
    # 'value_1': 300100000,
    # 'value_2': 25000000,
    # 'value_1': 250000,
    # 'value_2': 5001000,
    # 'value_1': 5643,
    # 'value_2': 10745,
    # 'value_1': 5,
    # 'value_2': 1000,
    # 'value_1': 5000,
    # 'value_2': 100,
    'value_1': 10000,
    'value_2': 55000,

    'font_size': 30
    }

create_diagram_page_8(context)


# # Размеры изображения
# img_1_width, img_2_width = create_diagram_page_8(context)


import os

pdf_file = "output.pdf"
page_number = 8
acrobat_path = fr"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
# Команда для открытия PDF в Adobe Acrobat на нужной странице
os.system(f'start "" "{acrobat_path}" /A "page={page_number}" "{pdf_file}"')