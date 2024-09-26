from insert_text import insert_texts
from insert_images import insert_images
from insert_niche_title import add_title
from create_diagram import create_diagram_page_8




contexts = [
    {
        'file_name': 'без данных.pdf',
        'page_num': 9,
        'font_size': 33,
        'font_path': 'Code-Pro-Bold-LC.ttf',
        'text': '5643',
        'color': (184 / 255, 1, 0),
        'coordinates': (390, 360),
        'output_path': 'output.pdf',
        'incremental': False
    },
    {
        'file_name': 'output.pdf',
        'page_num': 9,
        'font_size': 27,
        'font_path': 'Code-Pro-Bold-LC.ttf',
        'text': '10746',
        'color': (0, 0, 0),
        'coordinates': (420, 520),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 11,
        'font_size': 50,
        'font_path': 'Code-Pro-Bold-LC.ttf',
        'text': '43940',
        'color': (184 / 255, 1, 0),
        'coordinates': (750, 380),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 11,
        'font_size': 50,
        'font_path': 'Code-Pro-Bold-LC.ttf',
        'text': '248',
        'color': (184 / 255, 1, 0),
        'coordinates': (1180, 280),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 13,
        'font_size': 30,
        'font_path': 'CodePro/Code-Pro-LC.ttf',
        'text': '1-3',
        'color': (184 / 255, 1, 0),
        'coordinates': (413, 560),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 13,
        'font_size': 30,
        'font_path': 'CodePro/Code-Pro-LC.ttf',
        'text': '≈ 5000',
        'color': (184 / 255, 1, 0),
        'coordinates': (710, 95),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 11,
        'font_size': 50,
        'font_path': 'Code-Pro-Bold-LC.ttf',
        'text': '177',
        'color': (184 / 255, 1, 0),
        'coordinates': (1140, 680),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 14,
        'font_size': 30,
        'font_path': 'Jost-SemiBold.ttf',
        'text': '43940₽',
        'color': (0.94901, 0.41569, 0.35686),
        'coordinates': (445, 297),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 14,
        'font_size': 30,
        'font_path': 'Jost-SemiBold.ttf',
        'text': '30000₽',
        'color': (0.94901, 0.41569, 0.35686),
        'coordinates': (120, 360),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 14,
        'font_size': 30,
        'font_path': 'Jost-SemiBold.ttf',
        'text': '11940₽',
        'color': (0.94901, 0.41569, 0.35686),
        'coordinates': (120, 417),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 14,
        'font_size': 30,
        'font_path': 'Jost-SemiBold.ttf',
        'text': '2000₽',
        'color': (0.94901, 0.41569, 0.35686),
        'coordinates': (120, 480),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 14,
        'font_size': 30,
        'font_path': 'Jost-SemiBold.ttf',
        'text': '248',
        'color': (0.94901, 0.41569, 0.35686),
        'coordinates': (755, 365),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 14,
        'font_size': 30,
        'font_path': 'Jost-SemiBold.ttf',
        'text': '177₽',
        'color': (0.94901, 0.41569, 0.35686),
        'coordinates': (755, 423),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 14,
        'font_size': 30,
        'font_path': 'Jost-SemiBold.ttf',
        'text': '29900₽',
        'color': (0.94901, 0.41569, 0.35686),
        'coordinates': (805, 652),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 14,
        'font_size': 30,
        'font_path': 'Jost-SemiBold.ttf',
        'text': '“БАЗОВЫЙ”',
        'color': (0.94901, 0.41569, 0.35686),
        'coordinates': (1060, 652),
        'output_path': 'output.pdf',
        'incremental': True
    },
    {
        'file_name': 'output.pdf',
        'page_num': 14,
        'font_size': 30,
        'font_path': 'Jost-SemiBold.ttf',
        'text': '73840₽',
        'color': (0.94901, 0.41569, 0.35686),
        'coordinates': (1170, 695),
        'output_path': 'output.pdf',
        'incremental': True
    },
]

insert_texts(contexts)


contexts = [
    {
    'image_path': 'page_8-image_4.png',
    'file_name': 'output.pdf',
    'page_num': 8,
    'coordinates': (157, 283),
    'coef': 0.623,
    'output_path': 'output.pdf',
    'incremental': True
    },
    {
    'image_path': 'page_10-image_3.png',
    'file_name': 'output.pdf',
    'page_num': 10,
    'coordinates': (80, 287),
    'coef': 0.635,
    'output_path': 'output.pdf',
    'incremental': True
    },
    # {
    # 'image_path': 'Line 1.png',
    # 'file_name': 'output.pdf',
    # 'page_num': 7,
    # 'coordinates': (370, 283),
    # 'repeat_insertion': {
    #     'repeat_count': 5,
    #     'interval': 186,
    #     'direction': 'horizontal'
    #     },
    # 'coef': 1,
    # 'output_path': 'output.pdf',
    # 'incremental': True
    # },
    # {
    # 'image_path': 'output_image_1.png',
    # 'file_name': 'output.pdf',
    # 'page_num': 7,
    # 'coordinates': (376, 350),
    # 'coef': 1,
    # 'output_path': 'output.pdf',
    # 'incremental': True
    # },
    # {
    # 'image_path': 'output_image_2.png',
    # 'file_name': 'output.pdf',
    # 'page_num': 7,
    # 'coordinates': (376, 517),
    # 'coef': 1,
    # 'output_path': 'output.pdf',
    # 'incremental': True
    # }
]

context = {
    'file_name': 'output.pdf',
    'page_num': 7,
    'output_path': 'output.pdf',
    'incremental': True,
    'value_1': '5643',
    'value_2': '10745'
}

# create_diagram_page_8(context)


insert_images(contexts)



context = {
        'file_name': 'output.pdf',
        'page_num': 6,
        'font_size': 92,
        'font_path': 'Code-Pro-LC.ttf',
        'text': 'СТРОИТЕЛЬСТВО ДОМОВ В ПОДМОСКОВЬЕ И ЗАМОСКВОРЕЧЬЕ И ПОДМОСКВОРЕЧЬЕ ЧИЕ ЧИЕ',
        'color': (1, 1, 1),
        'y_coordinate': 420,
        'margin': 40,
        'output_path': 'output.pdf',
        'incremental': True
    }

add_title(context)

import os

pdf_file = "output.pdf"
page_number = 8
acrobat_path = fr"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
# Команда для открытия PDF в Adobe Acrobat на нужной странице
os.system(f'start "" "{acrobat_path}" /A "page={page_number}" "{pdf_file}"')