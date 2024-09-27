import os

pdf_file = "output.pdf"
page_number = 14
acrobat_path = fr"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
# Команда для открытия PDF в Adobe Acrobat на нужной странице
os.system(f'start "" "{acrobat_path}" /A "page={page_number}" "{pdf_file}"')