import fitz  # pymupdf

# Открытие существующего PDF-файла
pdf_document = fitz.open('Первичный анализ ниши.pdf')

# Выбор страницы, на которой нужно работать
page = pdf_document.load_page(0)  # Первая страница (индекс 0)

# Добавление текста на страницу
text = "Huyak!"
text_position = (100, 100)  # Позиция (x, y) для текста

# Создание объекта для добавления текста
page.insert_text(
    text_position,               # Позиция текста
    text,                        # Содержимое текста
    fontsize=75,                 # Размер шрифта
    color=(1, 0, 0)              # Цвет текста (RGB)
)

# Сохранение изменений в новый PDF-файл
pdf_document.save('output.pdf')
pdf_document.close()
