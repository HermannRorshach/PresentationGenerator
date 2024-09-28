from PIL import Image
import fitz
from .insert_images import insert_images
from .insert_text import insert_texts
from django.conf import settings
import os


context_scale_value = {
    'file_name': 'output.pdf',
    'page_num': 7,
    'font_size': 30,
    'font_path': 'fonts/CodePro/Code-Pro-Bold.ttf',
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
        'image_path': 'CreatePresentation/img/Line 1.png',
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
        'image_path': 'CreatePresentation/img/output_image_1.png',
        'file_name': 'output.pdf',
        'page_num': 7,
        'coordinates': (376, 350),
        'coef': 1,
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'image_path': 'CreatePresentation/img/output_image_2.png',
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
        'font_path': 'fonts/CodePro/Code-Pro-Bold.ttf',
        'text': '',
        'color': (1, 1, 1),
        'coordinates': [390, 390],
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 7,
        'font_size': 30,
        'font_path': 'fonts/CodePro/Code-Pro-Bold.ttf',
        'text': '',
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
    'font_path': 'fonts/CodePro/Code-Pro-Bold.ttf',
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

def create_color_rectanges(img_width, img_height, color, output_path):
    # Создание нового изображения
    image = Image.new("RGB", (img_width, img_height), color)

    # Сохранение изображения в формате PNG
    image.save(os.path.join(settings.BASE_DIR, f"CreatePresentation/{output_path}"))
    image.close()

def add_centered_text(contexts):
    # Открываем существующий PDF
    doc = fitz.open(os.path.join(settings.BASE_DIR, f"CreatePresentation/{contexts[0]['file_name']}"))

    for context in contexts:

        # Загружаем первую страницу для редактирования
        page = doc.load_page(context['page_num'])
        font_path = os.path.join(settings.BASE_DIR, f"CreatePresentation/{context['font_path']}")

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
    doc.save(os.path.join(settings.BASE_DIR, f"CreatePresentation/{context['output_path']}"), incremental=True, encryption=0)
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
    font = fitz.Font(fontfile=os.path.join(settings.BASE_DIR, f"CreatePresentation/{font_path}"))
    # Вычисляем ширину текста в точках
    text_width_actual = font.text_length(str(value), fontsize=context['font_size'])

    # Проверяем, поместится ли текст в указанный прямоугольник
    if text_width_actual > img_width:
        return False
    return True

def add_transparent_gap_to_line(input_image_path, output_image_path, gap_start, gap_height):
    # Открываем исходное изображение
    image = Image.open(os.path.join(settings.BASE_DIR, f"CreatePresentation/{input_image_path}")).convert("RGBA")

    # Получаем размеры исходного изображения
    width, height = image.size

    # Создаем новое изображение с таким же размером и поддержкой прозрачности
    new_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Копируем часть изображения до разрыва
    new_image.paste(image.crop((0, 0, width, gap_start)), (0, 0))

    # Копируем часть изображения после разрыва
    new_image.paste(image.crop((0, gap_start + gap_height, width, height)), (0, gap_start + gap_height))

    # Сохраняем новое изображение
    new_image.save(os.path.join(settings.BASE_DIR, f"CreatePresentation/{output_image_path}"), "PNG")

def handle_text_overflow(value_1, value_2, img_1_width, img_2_width, context):
    flag_1, flag_1_1, flag_2 = False, False, False
    interval = context_insert_images[0]['repeat_insertion']['interval']
    if (not is_text_fitting(value_1, 'fonts/CodePro/Code-Pro.ttf', img_1_width, context) and not is_text_fitting(value_1, 'fonts/CodePro/Code-Pro.ttf', abs(interval - img_1_width), context)) or (not is_text_fitting(value_2, 'fonts/CodePro/Code-Pro.ttf', img_2_width, context) and not is_text_fitting(value_2, 'fonts/CodePro/Code-Pro.ttf', abs(interval - img_2_width), context)):
        context_insert_images[0]['repeat_insertion']['repeat_count'] = 3
        print('Уменьшили количество линий')
    if not is_text_fitting(value_1, 'fonts/CodePro/Code-Pro.ttf', img_1_width, context):
        flag_1 = True
        if not is_text_fitting(value_1, 'fonts/CodePro/Code-Pro.ttf', abs(interval - img_1_width), context):
            input_image_path = 'CreatePresentation/img/Line 1.png'
            output_image_path = 'CreatePresentation/img/line_with_gap.png'
            gap_start = 67  # Начало разрыва (в пикселях)
            gap_height = 60  # Высота разрыва (в пикселях)
            flag_1_1 = True
            add_transparent_gap_to_line(input_image_path, output_image_path, gap_start, gap_height)
        contexts_for_values_in_side[0]['coordinates'][0] = 376 + img_1_width + 30
        contexts_for_values_in_side[0]['text'] = str(value_1)
        insert_texts([contexts_for_values_in_side[0]])

    if not is_text_fitting(value_2, 'fonts/CodePro/Code-Pro.ttf', img_2_width, context):
        flag_2 = True
        if not is_text_fitting(value_2, 'fonts/CodePro/Code-Pro.ttf', abs(interval - img_2_width), context):
            if flag_1_1:
                input_image_path = 'CreatePresentation/img/line_with_gap.png'
            else:
                input_image_path = 'CreatePresentation/img/Line 1.png'
            output_image_path = 'CreatePresentation/img/line_with_gap.png'
            gap_start = 234  # Начало разрыва (в пикселях)
            gap_height = 60  # Высота разрыва (в пикселях)

            add_transparent_gap_to_line(input_image_path, output_image_path, gap_start, gap_height)

        contexts_for_values_in_side[1]['coordinates'][0] = 376 + img_2_width + 30
        contexts_for_values_in_side[1]['text'] = str(value_2)
        insert_texts([contexts_for_values_in_side[1]])

    context_lines = [
        {
            'image_path': 'CreatePresentation/img/Line 1.png',
            'file_name': 'output.pdf',
            'page_num': 7,
            'coordinates': (370, 283),
            'coef': 1,
            'output_path': 'output.pdf',
            'incremental': True
        },
        {
            'image_path': 'CreatePresentation/img/line_with_gap.png',
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

def replace_images_with_squares():
    image_paths = [
        'CreatePresentation/img/search_view_cost_1.png',
        'CreatePresentation/img/recommendation_view_cost_1.png',
        'CreatePresentation/img/search_view_cost_2.png',
        'CreatePresentation/img/recommendation_view_cost_2.png',
        'CreatePresentation/img/search_view_cost_3.png',
        'CreatePresentation/img/recommendation_view_cost_3.png',
        'CreatePresentation/img/output_image_1.png',
        'CreatePresentation/img/output_image_2.png'
    ]
    for img_path in image_paths:
        # Заменяем каждое изображение на прозрачный квадрат 1x1
        square = Image.new("RGBA", (1, 1), (255, 255, 255, 0))  # Прозрачный квадрат
        square.save(img_path)  # Сохраняем с тем же именем

from datetime import datetime

def create_new_document():
    # Создаем имя нового документа по текущей дате и времени
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_pdf_path = f"new_document_{timestamp}.pdf"

    # Открываем PDF файл и извлекаем 8-ю страницу
    with fitz.open(os.path.join(settings.BASE_DIR, f"CreatePresentation/Без данных.pdf")) as source_pdf:
        new_pdf = fitz.open()  # Создаем новый PDF
        page_8 = source_pdf[7]  # Индексация страниц начинается с 0
        new_pdf.insert_page(-1)  # Создаем пустую страницу в новом документе
        new_pdf.insert_page(-1, from_page=page_8)
        new_pdf.save(os.path.join(settings.BASE_DIR, f"CreatePresentation/{new_pdf_path}"))
    d = context_scale_value
    d['file_name'] = new_pdf_path
    d['page_num'] = 0
    d['output_path'] = new_pdf_path

    for d in context_insert_images:
        d['file_name'] = new_pdf_path
        d['page_num'] = 0
        d['output_path'] = new_pdf_path

    for d in contexts_for_values_in_side:
        d['file_name'] = new_pdf_path
        d['page_num'] = 0
        d['output_path'] = new_pdf_path


    for d in context_values_in_rectangles:
        d['file_name'] = new_pdf_path
        d['page_num'] = 0
        d['output_path'] = new_pdf_path

    return new_pdf_path

def replace_page_with_new_document(original_pdf_path, new_pdf_path, page_number):
    # Открываем оригинальный PDF и новый PDF
    with fitz.open(os.path.join(settings.BASE_DIR, f"CreatePresentation/{original_pdf_path}")) as original_pdf:
        with fitz.open(os.path.join(settings.BASE_DIR, f"CreatePresentation/{new_pdf_path}")) as new_pdf:
            # Удаляем 8-ю страницу (индекс 7)
            original_pdf.delete_page(page_number - 1)
            # Вставляем новую страницу на место удаленной
            original_pdf.insert_pdf(new_pdf, from_page=0, to_page=0, at_page=page_number - 1)
            # Сохраняем изменения в оригинальном PDF
            original_pdf.save(settings.BASE_DIR, f"CreatePresentation/{original_pdf_path}")




def create_diagram_page_8(context):
    # replace_images_with_squares()
    # new_pdf_path = create_new_document()


    value_1 = context['value_1']
    value_2 = context['value_2']

    img_1_width, img_2_width, scale_marks = calculate_scale_and_widths(value_1, value_2)

    img_height = 60

    # Цвет (в формате RGB)
    color_1 = (255, 255, 255)  # Цвет B8FF00 в формате RGB
    color_2 = (184, 255, 0)

    create_color_rectanges(img_1_width, img_height, color_1, "img/output_image_1.png")
    create_color_rectanges(img_2_width, img_height, color_2, "img/output_image_2.png")

    context_values_in_rectangles[0]['x_center'] = 370 + img_1_width / 2
    context_values_in_rectangles[0]['text'] = str(value_1)
    copy = {key: value for key, value in context_values_in_rectangles[0].items()}
    copy['x_center'] = 370 + img_2_width / 2
    copy['text'] = str(value_2)
    copy['y_coordinate'] = 536
    context_values_in_rectangles.append(copy)

    if (is_text_fitting(value_1, 'fonts/CodePro/Code-Pro.ttf', img_1_width, context) and is_text_fitting(value_2, 'fonts/CodePro/Code-Pro.ttf', img_2_width, context)):
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
    # replace_page_with_new_document(os.path.join(settings.BASE_DIR, f"CreatePresentation/outputepdf"), new_pdf_path, 8)

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

# create_diagram_page_8(context)

contexts_page_10 = [
    {
        'file_name': 'output.pdf',
        'page_num': 9,
        'font_size': 25,
        'font_path': 'fonts/CodePro/Code-Pro-Bold.ttf',
        'text': 'ЦЕНА ПРОСМОТРА',
        'color': (1, 1, 1),
        'coordinates': (381, 300),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 9,
        'font_size': 25,
        'font_path': 'fonts/CodePro/Code-Pro-Bold.ttf',
        'text': 'КОНВЕРСИЯ В КОНТАКТ',
        'color': (1, 1, 1),
        'coordinates': (691, 300),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 9,
        'font_size': 25,
        'font_path': 'fonts/CodePro/Code-Pro-Bold.ttf',
        'text': 'ЦЕНА КОНТАКТА',
        'color': (1, 1, 1),
        'coordinates': (1071, 300),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 9,
        'font_size': 25,
        'font_path': 'fonts/CodePro/Code-Pro.ttf',
        'text': 'Значение поисковой выдачи',
        'color': (1, 1, 1),
        'coordinates': (1071, 300),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 9,
        'font_size': 25,
        'font_path': 'fonts/CodePro/Code-Pro.ttf',
        'text': 'Значение рекомендаций',
        'color': (1, 1, 1),
        'coordinates': (1071, 300),
        'output_path': 'output.pdf',
        'incremental': True
    },
]

context_insert_images_page_10 = [
    {
        'image_path': 'CreatePresentation/img/Line 1.png',
        'file_name': 'output.pdf',
        'page_num': 9,
        'coordinates': (370, 320),
        'coef': 1,
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'image_path': 'CreatePresentation/img/Line 1.png',
        'file_name': 'output.pdf',
        'page_num': 9,
        'coordinates': (680, 320),
        'repeat_insertion': {
            'repeat_count': 2,
            'interval': 380,
            'direction': 'horizontal_asc'
            },
        'coef': 1,
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'image_path': 'CreatePresentation/img/search_view_cost_1.png',
        'file_name': 'output.pdf',
        'page_num': 9,
        'coordinates': [376, 390],
        'coef': 1,
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'image_path': 'CreatePresentation/img/recommendation_view_cost_1.png',
        'file_name': 'output.pdf',
        'page_num': 9,
        'coordinates': [376, 560],
        'coef': 1,
        'output_path': 'output.pdf',
        'incremental': True
    }
]

# context_page_10 = {
#     'search_view_cost': '15',
#     'search_contact_conversion_rate': '6',
#     'search_contact_cost': '300',
#     'recommendation_view_cost': '27',
#     'recommendation_contact_conversion_rate': '5',
#     'recommendation_contact_cost': '150'
# }

def calculate_rectangle_widths(max_width, search_value, recommendation_value):
    # Находим максимальное значение
    max_value = max(search_value, recommendation_value)

    # Вычисляем процент меньшего значения
    if max_value == search_value:
        smaller_value = recommendation_value
        smaller_key = 'recommendation'
        larger_key = 'search'
    else:
        smaller_value = search_value
        smaller_key = 'search'
        larger_key = 'recommendation'

    # Вычисляем процент от максимального значения
    smaller_value_percent = (smaller_value / max_value) * 100

    # Вычисляем ширину прямоугольника для меньшего значения
    smaller_rect_width = (max_width * smaller_value_percent) / 100

    # Возвращаем словарь с ширинами прямоугольников
    return {
        larger_key: max_width,           # Ширина для большего значения
        smaller_key: int(smaller_rect_width)  # Ширина для меньшего значения
    }

def create_diagram_page_10(context):
    search_view_cost = context['search_view_cost']
    search_contact_conversion_rate = context ['search_contact_conversion_rate']
    search_contact_cost = context['search_contact_cost']

    recommendation_view_cost = context['recommendation_view_cost']
    recommendation_contact_conversion_rate = context ['recommendation_contact_conversion_rate']
    recommendation_contact_cost = context['recommendation_contact_cost']

    view_cost = calculate_rectangle_widths(200, int(search_view_cost), int(recommendation_view_cost))
    conversion_rate = calculate_rectangle_widths(200, int(search_contact_conversion_rate.split('.')[0]), int(recommendation_contact_conversion_rate.split('.')[0]))
    contact_cost = calculate_rectangle_widths(200, int(search_contact_cost.split('.')[0]), int(recommendation_contact_cost.split('.')[0]))

    for index, dictionary in enumerate((view_cost, conversion_rate, contact_cost), start=1):
        img_1_width = dictionary['search']
        img_2_width = dictionary['recommendation']
        img_height = 60
        color_1 = (255, 255, 255)
        color_2 = (184, 255, 0)
        output_path_1 = f"img/search_view_cost_{index}.png"
        output_path_2 = f"img/recommendation_view_cost_{index}.png"
        # Создаём цветные прямоугольники для диаграмм
        create_color_rectanges(img_1_width, img_height, color_1, output_path_1)
        create_color_rectanges(img_2_width, img_height, color_2, output_path_2)

    for tpl in (
        ('CreatePresentation/img/search_view_cost_1.png', 'CreatePresentation/img/recommendation_view_cost_1.png', 376),
        ('CreatePresentation/img/search_view_cost_2.png', 'CreatePresentation/img/recommendation_view_cost_2.png', 686),
        ('CreatePresentation/img/search_view_cost_3.png', 'CreatePresentation/img/recommendation_view_cost_3.png', 1066)
        ):
        first_img = {key: value for key, value in context_insert_images_page_10[2].items()}
        second_img = {key: value for key, value in context_insert_images_page_10[3].items()}
        first_img['image_path'] = tpl[0]
        first_img['coordinates'] = [tpl[2], context_insert_images_page_10[2]['coordinates'][1]]
        second_img['image_path'] = tpl[1]
        second_img['coordinates'] = [tpl[2], context_insert_images_page_10[3]['coordinates'][1]]

        context_insert_images_page_10.extend([first_img, second_img])

    del context_insert_images_page_10[2:4]

    # Вставляем текст со значениями справа от диаграмм
    for index, tpl in enumerate((
        (search_view_cost, recommendation_view_cost, view_cost),
        (search_contact_conversion_rate, recommendation_contact_conversion_rate, conversion_rate),
        (search_contact_cost, recommendation_contact_cost, contact_cost)
        )):
        first_line = {key: value for key, value in contexts_page_10[3].items()}
        second_line = {key: value for key, value in contexts_page_10[4].items()}
        first_line['text'] = str(tpl[0])
        x = context_insert_images_page_10[2 + index * 2]['coordinates'][0] + tpl[2]['search'] + 30
        y = context_insert_images_page_10[2 + index * 2]['coordinates'][1] + 40

        first_line['coordinates'] = [x, y]
        second_line['text'] = str(tpl[1])
        x = context_insert_images_page_10[2 + index * 2 + 1]['coordinates'][0] + tpl[2]['recommendation'] + 30
        y = context_insert_images_page_10[2 + index * 2 + 1]['coordinates'][1] + 40
        second_line['coordinates'] = [x, y]

        contexts_page_10.extend([first_line, second_line])
    del contexts_page_10[3:5]

    insert_images(context_insert_images_page_10)
    insert_texts(contexts_page_10)

# create_diagram_page_10(context=context_page_10)




import os

pdf_file = "output.pdf"
page_number = 10
acrobat_path = fr"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
# Команда для открытия PDF в Adobe Acrobat на нужной странице
# os.system(f'start "" "{acrobat_path}" /A "page={page_number}" "{pdf_file}"')