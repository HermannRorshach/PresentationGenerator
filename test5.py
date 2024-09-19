from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Создание нового PDF с текстом
pdf_path = 'text_with_custom_font.pdf'
c = canvas.Canvas(pdf_path, pagesize=letter)

# Регистрация кастомного шрифта
font_path = 'Montserrat-SemiBold.ttf'
pdfmetrics.registerFont(TTFont('CustomFont', font_path))
c.setFont('CustomFont', 12)

# Добавление текста
c.drawString(100, 700, "Huyak! Яблоко-малина!")
c.save()
