import fitz  # pymupdf

# Открытие существующего PDF-файла
pdf_document = fitz.open('Первичный анализ ниши.pdf')

# Выбор страницы, на которой нужно работать
page = pdf_document.load_page(0)  # Первая страница (индекс 0)

# Настройка шрифта и его стиля
font_path = 'Jost-VariableFont_wght.ttf'  # Путь к файлу шрифта
text = "Huyak! Яблоко-малина!"
text_position = (100, 100)  # Позиция (x, y) для текста

# Загрузка шрифта
font = fitz.Font(fontfile=font_path)

# Добавление текста на страницу
page.insert_text(
    text_position,              # Позиция текста
    text,                       # Содержимое текста
    fontsize=78,                # Размер шрифта
    color=(1, 0, 0)             # Цвет текста (в диапазоне от 0 до 1)
)

# Сохранение изменений в новый PDF-файл
pdf_document.save('output.pdf')
pdf_document.close()
