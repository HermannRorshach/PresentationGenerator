import fitz  # pymupdf


def insert_text(context):

# Открытие существующего PDF-файла
    pdf_document = fitz.open(context['file_name'])

# Выбор страницы, на которой нужно работать
    page = pdf_document.load_page(context['page_num'])  # Первая страница (индекс 0)

# Путь к кастомному шрифту
    font_path = context['font_path']

# Вставка кастомного шрифта на страницу
    fontname = 'CustomFont'
    page.insert_font(fontfile=font_path, fontname=fontname)

# Настройка шрифта и текста
    text = context['text']
    text_position = context['coordinates']   # Позиция (x, y) для текста

# Добавление текста на страницу с использованием кастомного шрифта
    page.insert_text(
        text_position,              # Позиция текста
        text,                       # Содержимое текста
        fontsize=33,                # Размер шрифта
        fontname=fontname,          # Имя кастомного шрифта
        color=context['color']             # Цвет текста (в диапазоне от 0 до 1)
    )

# Сохранение изменений в новый PDF-файл
    pdf_document.save(context['output_path'], incremental=context['incremental'], encryption=0)
    pdf_document.close()


context = {
    'file_name': 'Первичный анализ ниши пустая презентация.pdf',
    'page_num': 9,
    'font_size': 33,
    'font_path': 'Code-Pro-Bold-LC.ttf',
    'text': '5643',
    'color': (184 / 255, 1, 0),
    'coordinates': (390, 360),
    'output_path': 'output.pdf',
    'incremental': False
    }

insert_text(context)

context = {
    'file_name': 'output.pdf',
    'page_num': 9,
    'font_size': 27,
    'font_path': 'Code-Pro-Bold-LC.ttf',
    'text': '10746',
    'color': (0, 0, 0),
    'coordinates': (420, 520),
    'output_path': 'output.pdf',
    'incremental': True
    }

insert_text(context)
