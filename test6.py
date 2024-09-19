import fitz  # pymupdf

# Открытие существующего PDF-файла
pdf_document = fitz.open('Первичный анализ ниши.pdf')

# Выбор страницы, на которой нужно работать
page = pdf_document.load_page(0)  # Первая страница (индекс 0)

# Путь к кастомному шрифту
font_path = 'Jost-SemiBold.ttf'

# Вставка кастомного шрифта на страницу
fontname = 'CustomFont'
page.insert_font(fontfile=font_path, fontname=fontname)

# Настройка шрифта и текста
text = "Huyak! Яблоко-малина!"
text_position = (150, 200)  # Позиция (x, y) для текста

# Добавление текста на страницу с использованием кастомного шрифта
page.insert_text(
    text_position,              # Позиция текста
    text,                       # Содержимое текста
    fontsize=78,                # Размер шрифта
    fontname=fontname,          # Имя кастомного шрифта
    color=(1, 0, 0)             # Цвет текста (в диапазоне от 0 до 1)
)

# Сохранение изменений в новый PDF-файл
pdf_document.save('output.pdf')
pdf_document.close()
