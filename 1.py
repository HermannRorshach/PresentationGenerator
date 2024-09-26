import fitz

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
        font = fitz.Font(fontfile=font_path)

        # Вычисляем ширину текста в точках
        text_width_actual = font.text_length(context['text'], fontsize=context['font_size'])

        # Проверяем, поместится ли текст в указанный прямоугольник
        if text_width_actual > text_width:
            print('Текст не помещается в указанный прямоугольник')
        else:
            print('Текст помещается')


    # Сохраняем изменения в новый файл
    doc.save(context['output_path'], incremental=True, encryption=0)
    doc.close()

contexts = [
    {
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
        },
        {
        'file_name': 'output.pdf',
        'page_num': 7,
        'font_size': 30,
        'font_path': 'Code-Pro-Bold-LC.ttf',
        'text': '2000000000',
        'color': (1, 1, 1),
        'y_coordinate': 700,
        'x_center': 742,  # Центр текста по оси X
        'text_width': 180,  # Ширина текстового блока
        'margin': 10,
        'output_path': 'output.pdf',
        'incremental': True
        },
        {
        'file_name': 'output.pdf',
        'page_num': 7,
        'font_size': 30,
        'font_path': 'Code-Pro-Bold-LC.ttf',
        'text': '30000000000',
        'color': (1, 1, 1),
        'y_coordinate': 700,
        'x_center': 928,
        'text_width': 180,
        'margin': 10,
        'output_path': 'output.pdf',
        'incremental': True
        },
        {
        'file_name': 'output.pdf',
        'page_num': 7,
        'font_size': 30,
        'font_path': 'Code-Pro-Bold-LC.ttf',
        'text': '300000000',
        'color': (1, 1, 1),
        'y_coordinate': 700,
        'x_center': 928,
        'text_width': 180,
        'margin': 10,
        'output_path': 'output.pdf',
        'incremental': True
        }
]

add_centered_text(contexts)

import os

pdf_file = "output.pdf"
page_number = 8
acrobat_path = fr"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
# Команда для открытия PDF в Adobe Acrobat на нужной странице
os.system(f'start "" "{acrobat_path}" /A "page={page_number}" "{pdf_file}"')
