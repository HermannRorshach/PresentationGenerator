import fitz  # pymupdf
from django.conf import settings
import os



def insert_texts(contexts):

    # Открытие существующего PDF-файла
    doc = fitz.open(os.path.join(settings.BASE_DIR, f"CreatePresentation/{contexts[0]['file_name']}"))
    incremental = contexts[0]['incremental']
    output_path = contexts[0]['output_path']

    for index, context in enumerate(contexts):

        if not context['incremental'] == incremental or not context['output_path'] == output_path:
            doc.save(os.path.join(settings.BASE_DIR, f"CreatePresentation/{contexts[index - 1]['output_path']}"), incremental=contexts[index - 1]['incremental'], encryption=0)
            doc.close()
            incremental = contexts[index]['incremental']
            output_path = contexts[index]['output_path']
            doc = fitz.open(os.path.join(settings.BASE_DIR, f"CreatePresentation/{contexts[index]['file_name']}"))

        # Выбор страницы, на которой нужно работать
        page = doc.load_page(context['page_num'])  # Первая страница (индекс 0)

        # Путь к кастомному шрифту
        font_path = os.path.join(settings.BASE_DIR, f"CreatePresentation/{context['font_path']}")

        # Вставка кастомного шрифта на страницу
        fontname = os.path.splitext(os.path.basename(context['font_path']))[0]
        page.insert_font(fontfile=font_path, fontname=fontname)

        # Настройка шрифта и текста
        text = context['text']
        text_position = context['coordinates']   # Позиция (x, y) для текста

        # Добавление текста на страницу с использованием кастомного шрифта
        page.insert_text(
            text_position,              # Позиция текста
            text,                       # Содержимое текста
            fontsize=context['font_size'],                # Размер шрифта
            fontname=fontname,          # Имя кастомного шрифта
            color=context['color']             # Цвет текста (в диапазоне от 0 до 1)
        )

# Сохранение изменений в новый PDF-файл
    doc.save(os.path.join(settings.BASE_DIR, f"CreatePresentation/{context['output_path']}"), incremental=context['incremental'], encryption=0)
    doc.close()
