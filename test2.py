import fitz  # PyMuPDF

# Открываем PDF-файл
doc = fitz.open("Первичный анализ ниши.pdf")

# Проходим по всем страницам документа
for page_num in range(doc.page_count):
    page = doc[page_num]
    print(f"Страница {page_num + 1}")

    # Извлекаем текст с текущей страницы
    text = page.get_text("text")
    if not text:
        print(f"Ошибка извлечения текста на странице {page_num + 1}")
        continue

    if "Avito" in text:
        print("Найдено слово 'Avito'")

        # Ищем все вхождения слова
        text_instances = page.search_for("Avito")
        print(f"Найдено {len(text_instances)} вхождений на странице")

        # Заменяем найденные вхождения
        for inst in text_instances:
            try:
                # Наложение нового текста на место старого
                page.insert_text((inst.x0, inst.y0), "Huito!", fontsize=12, color=(0, 0, 0))
                print(f"Заменено вхождение на позиции {inst}")
            except Exception as e:
                print(f"Ошибка при замене: {e}")
    else:
        print(f"Слово 'Avito' не найдено на странице {page_num + 1}, но текст извлечён.")

# Сохраняем изменения в новом файле
doc.save("output.pdf")
doc.close()
