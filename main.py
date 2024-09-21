from insert_text import insert_text
from insert_image import insert_image


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

# context = {
#     'file_name': 'output.pdf',
#     'page_num': 9,
#     'font_size': 27,
#     'font_path': 'Code-Pro-Bold-LC.ttf',
#     'text': '10746',
#     'color': (0, 0, 0),
#     'coordinates': (420, 520),
#     'output_path': 'output.pdf',
#     'incremental': True
#     }

# insert_text(context)

# context = {
#     'file_name': 'output.pdf',
#     'page_num': 11,
#     'font_size': 50,
#     'font_path': 'Code-Pro-Bold-LC.ttf',
#     'text': '43940',
#     'color': (184 / 255, 1, 0),
#     'coordinates': (750, 380),
#     'output_path': 'output.pdf',
#     'incremental': True
#     }

# insert_text(context)

# context = {
#     'file_name': 'output.pdf',
#     'page_num': 11,
#     'font_size': 50,
#     'font_path': 'Code-Pro-Bold-LC.ttf',
#     'text': '248',
#     'color': (184 / 255, 1, 0),
#     'coordinates': (1180, 280),
#     'output_path': 'output.pdf',
#     'incremental': True
#     }

# insert_text(context)

# context = {
#     'file_name': 'output.pdf',
#     'page_num': 11,
#     'font_size': 50,
#     'font_path': 'Code-Pro-Bold-LC.ttf',
#     'text': '177',
#     'color': (184 / 255, 1, 0),
#     'coordinates': (1140, 680),
#     'output_path': 'output.pdf',
#     'incremental': True
#     }

# insert_text(context)


# context = {
#     'image_path': 'page_8-image_4.png',
#     'file_name': 'output.pdf',
#     'page_num': 8,
#     'coordinates': (160, 253),
#     'coef': 0.62,
#     'output_path': 'output.pdf',
#     'incremental': True
# }

# insert_image(context)

# context = {
#     'image_path': 'page_10-image_3.png',
#     'file_name': 'output.pdf',
#     'page_num': 10,
#     'coordinates': (100, 253),
#     'coef': 0.65,
#     'output_path': 'output.pdf',
#     'incremental': True
# }

# insert_image(context)

context = {
    'image_path': 'fon_pillow_paste.png',
    'file_name': 'output.pdf',
    'page_num': 9,
    'coordinates': (100, 253),
    'coef': 1.55,
    'output_path': 'output.pdf',
    'incremental': True
}

insert_image(context)