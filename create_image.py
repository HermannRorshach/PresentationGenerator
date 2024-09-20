from PIL import Image

# Размеры изображения
img_width = 1000
img_height = 300

# Цвет (в формате RGB)
color = (184, 255, 0)  # Цвет B8FF00 в формате RGB

# Создание нового изображения
image = Image.new("RGB", (img_width, img_height), color)

# Сохранение изображения в формате PNG
image.save("output_image.png")
