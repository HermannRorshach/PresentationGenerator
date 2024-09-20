import pandas as pd

# Загрузка Excel файла
file_path = 'Товары Первичный анализ ниши CLICKAVO.xlsx'
xls = pd.ExcelFile(file_path)

# Извлечение данных из последнего листа
last_sheet = xls.sheet_names[-1]
last_sheet_data = pd.read_excel(xls, sheet_name=last_sheet)
print(xls.sheet_names)

# Извлечение данных с листа "Общий (копия)"
common_copy_data = pd.read_excel(xls, sheet_name="presentation_data")

# Вывод данных
print("Данные из последнего листа:")
print(last_sheet_data)

print("\nДанные из листа 'presentation_data':")
print(common_copy_data)

last_row = last_sheet_data.iloc[-1]

# Вывод последней строки
print("Последняя строка на листе:")
print(last_row)
