from PIL import Image, ImageDraw

def add_transparent_gap_to_line(input_image_path, output_image_path, gap_start, gap_height):
    # Открываем исходное изображение
    image = Image.open(input_image_path).convert("RGBA")

    # Получаем размеры исходного изображения
    width, height = image.size

    # Создаем новое изображение с таким же размером и поддержкой прозрачности
    new_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Копируем часть изображения до разрыва
    new_image.paste(image.crop((0, 0, width, gap_start)), (0, 0))

    # Копируем часть изображения после разрыва
    new_image.paste(image.crop((0, gap_start + gap_height, width, height)), (0, gap_start + gap_height))

    # Сохраняем новое изображение
    new_image.save(output_image_path, "PNG")
    new_image.show()

# Пример использования
input_image_path = 'line_with_gap.png'
output_image_path = 'line_with_gap.png'
gap_start = 230  # Начало разрыва (в пикселях)
gap_height = 10  # Высота разрыва (в пикселях)

add_transparent_gap_to_line(input_image_path, output_image_path, gap_start, gap_height)
