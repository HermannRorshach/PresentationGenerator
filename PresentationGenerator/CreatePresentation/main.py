from .insert_text import insert_texts
from .insert_images import insert_images
from .insert_niche_title import add_title
from .create_diagram import create_diagram_page_8, create_diagram_page_10
from .add_centered_text import add_centered_text
import pandas as pd
from django.conf import settings
import os
from datetime import datetime
from datetime import datetime
import pytz


def extract_data(file_path):
    with pd.ExcelFile(file_path) as xls:  # Контекстный менеджер закроет файл после использования
        # Извлечение данных с листа "Для разработчика" без заголовков
        presentation_data = pd.read_excel(xls, sheet_name="Для разработчика", header=None, dtype=str)

        # Устанавливаем первый столбец как индекс
        presentation_data.set_index(0, inplace=True)

        # Присваиваем значения переменным, используя индексы
        all_data = {
            'views_search': presentation_data.loc["Просмотры в поисковой выдаче"].values[0],
            'views_recommendations': presentation_data.loc["Просмотры в рекомендациях"].values[0],
            'cost_per_view_search': f"{round(float(presentation_data.loc['Цена просмотра в поисковой выдачи'].values[0]), 1)}",
            'cost_per_view_recommendations': f"{round(float(presentation_data.loc['Цена просмотра в рекомендациях'].values[0]), 1)}",
            'conversion_rate_search': f"{float(presentation_data.loc['Конверсия в контакт в поисковой выдаче'].values[0]) * 100:.1f}%",
            'conversion_rate_recommendations': f"{float(presentation_data.loc['Конверсия в контакт в рекомендациях'].values[0]) * 100:.1f}%",
            'cost_per_contact_search': f"{round(float(presentation_data.loc['Цена контакта в поисковой выдаче'].values[0]))}",
            'cost_per_contact_recommendations': f"{round(float(presentation_data.loc['Цена контакта в рекомендациях'].values[0]))}",
            'optimal_ad_budget': f"{round(float(presentation_data.loc['Оптимальный рекламный бюджет'].values[0]))}",
            'total_contacts': f"{round(float(presentation_data.loc['Количество контактов'].values[0]))}",
            'average_contact_cost': f"{round(float(presentation_data.loc['Средняя стоимость контакта'].values[0]))}",
            'all_ads_count': presentation_data.loc["Публикация объявлений"].values[0],
            'ad_promotion_range': presentation_data.loc["Продвижение объявлений"].values[0],
            'budget_views_ads': f"{round(float(presentation_data.loc['Бюджет на просмотры/объявления'].values[0]))}",
            'budget_promotion_services': f"{round(float(presentation_data.loc['Бюджет на услуги продвижения'].values[0]))}",
            'avito_tariff_budget': f"{round(float(presentation_data.loc['Бюджет на тариф авито'].values[0]))}",
            'agency_service_cost': f"{round(float(presentation_data.loc['Стоимость услуг агентства'].values[0]))}",
            'tariff_name': presentation_data.loc["Название тарифа"].values[0],
            'total_ad_budget': f"{round(float(presentation_data.loc['Суммарный рекламный бюджет'].values[0]))}",
            'niche': presentation_data.loc["Ниша"].values[0]
        }
    return all_data

# Получение данных из файла
# all_data = extract_data('Первичный анализ ниши 9-13 Для презентации.xlsx')


def main(all_data, first_image, second_image):
    # Присвоение значений переменным
    views_search = all_data['views_search']
    views_recommendations = all_data['views_recommendations']
    cost_per_view_search = all_data['cost_per_view_search']
    cost_per_view_recommendations = all_data['cost_per_view_recommendations']
    conversion_rate_search = all_data['conversion_rate_search']
    conversion_rate_recommendations = all_data['conversion_rate_recommendations']
    cost_per_contact_search = all_data['cost_per_contact_search']
    cost_per_contact_recommendations = all_data['cost_per_contact_recommendations']
    optimal_ad_budget = all_data['optimal_ad_budget']
    total_contacts = all_data['total_contacts']
    average_contact_cost = all_data['average_contact_cost']
    all_ads_count = all_data['all_ads_count']
    ad_promotion_range = all_data['ad_promotion_range']
    budget_views_ads = all_data['budget_views_ads']
    budget_promotion_services = all_data['budget_promotion_services']
    avito_tariff_budget = all_data['avito_tariff_budget']
    agency_service_cost = all_data['agency_service_cost']
    tariff_name = all_data['tariff_name']
    total_ad_budget = all_data['total_ad_budget']
    niche = all_data['niche']


    contexts = [
        {
            'file_name': 'без данных.pdf',
            'page_num': 9,
            'font_size': 33,
            'font_path': 'fonts/CodePro/Code-Pro-Bold.ttf',
            'text': '',
            'color': (184 / 255, 1, 0),
            'coordinates': (390, 360),
            'output_path': 'output.pdf',
            'incremental': False
        },
        {
            'file_name': 'output.pdf',
            'page_num': 13,
            'font_size': 30,
            'font_path': 'fonts/CodePro/Code-Pro.ttf',
            'text': ad_promotion_range,
            'color': (184 / 255, 1, 0),
            'coordinates': (413, 560),
            'output_path': 'output.pdf',
            'incremental': True
        },
        {
            'file_name': 'output.pdf',
            'page_num': 13,
            'font_size': 30,
            'font_path': 'fonts/CodePro/Code-Pro.ttf',
            'text': all_ads_count,
            'color': (184 / 255, 1, 0),
            'coordinates': (710, 95),
            'output_path': 'output.pdf',
            'incremental': True
        },
        {
            'file_name': 'output.pdf',
            'page_num': 14,
            'font_size': 30,
            'font_path': 'fonts/Jost-Regular.ttf',
            'text': f"{optimal_ad_budget}₽",
            'color': (0.94901, 0.41569, 0.35686),
            'coordinates': (445, 297),
            'output_path': 'output.pdf',
            'incremental': True
        },
        {
            'file_name': 'output.pdf',
            'page_num': 14,
            'font_size': 30,
            'font_path': 'fonts/Jost-Regular.ttf',
            'text': f"{budget_views_ads}₽",
            'color': (0.94901, 0.41569, 0.35686),
            'coordinates': (120, 360),
            'output_path': 'output.pdf',
            'incremental': True
        },
        {
            'file_name': 'output.pdf',
            'page_num': 14,
            'font_size': 30,
            'font_path': 'fonts/Jost-Regular.ttf',
            'text': f"{budget_promotion_services}₽",
            'color': (0.94901, 0.41569, 0.35686),
            'coordinates': (120, 417),
            'output_path': 'output.pdf',
            'incremental': True
        },
        {
            'file_name': 'output.pdf',
            'page_num': 14,
            'font_size': 30,
            'font_path': 'fonts/Jost-Regular.ttf',
            'text': f"{avito_tariff_budget}₽",
            'color': (0.94901, 0.41569, 0.35686),
            'coordinates': (120, 480),
            'output_path': 'output.pdf',
            'incremental': True
        },
        {
            'file_name': 'output.pdf',
            'page_num': 14,
            'font_size': 30,
            'font_path': 'fonts/CodePro/Code-Pro.ttf',
            'text': total_contacts,
            'color': (0.94901, 0.41569, 0.35686),
            'coordinates': (755, 365),
            'output_path': 'output.pdf',
            'incremental': True
        },
        {
            'file_name': 'output.pdf',
            'page_num': 14,
            'font_size': 30,
            'font_path': 'fonts/Jost-Regular.ttf',
            'text': f"{average_contact_cost}₽",
            'color': (0.94901, 0.41569, 0.35686),
            'coordinates': (755, 423),
            'output_path': 'output.pdf',
            'incremental': True
        },
        {
            'file_name': 'output.pdf',
            'page_num': 14,
            'font_size': 30,
            'font_path': 'fonts/Jost-Regular.ttf',
            'text': f"{agency_service_cost}₽",
            'color': (0.94901, 0.41569, 0.35686),
            'coordinates': (805, 652),
            'output_path': 'output.pdf',
            'incremental': True
        },
        {
            'file_name': 'output.pdf',
            'page_num': 14,
            'font_size': 30,
            'font_path': 'fonts/CodePro/Code-Pro.ttf',
            'text': tariff_name,
            'color': (0.94901, 0.41569, 0.35686),
            'coordinates': (1060, 652),
            'output_path': 'output.pdf',
            'incremental': True
        },
        {
            'file_name': 'output.pdf',
            'page_num': 14,
            'font_size': 30,
            'font_path': 'fonts/Jost-Regular.ttf',
            'text': f"{total_ad_budget}₽",
            'color': (0.94901, 0.41569, 0.35686),
            'coordinates': (1170, 695),
            'output_path': 'output.pdf',
            'incremental': True
        },
    ]

    insert_texts(contexts)

    contexts = [
        {
            'file_name': 'output.pdf',
            'page_num': 11,
            'font_size': 50,
            'font_path': 'fonts/CodePro/Code-Pro.ttf',
            'text': optimal_ad_budget,
            'color': (184 / 255, 1, 0),
            'coordinates': (750, 380),
            'y_coordinate':350,
            'x_center': 820,
            'text_width': 300,
            'output_path': 'output.pdf',
            'incremental': True
        },
        {
            'file_name': 'output.pdf',
            'page_num': 11,
            'font_size': 50,
            'font_path': 'fonts/CodePro/Code-Pro.ttf',
            'text': total_contacts,
            'color': (184 / 255, 1, 0),
            'coordinates': (1180, 280),
            'y_coordinate':250,
            'x_center': 1230,
            'text_width': 300,
            'output_path': 'output.pdf',
            'incremental': True
        },
        {
            'file_name': 'output.pdf',
            'page_num': 11,
            'font_size': 50,
            'font_path': 'fonts/CodePro/Code-Pro.ttf',
            'text': average_contact_cost,
            'color': (184 / 255, 1, 0),
            'coordinates': (1140, 680),
            'y_coordinate': 640,
            'x_center': 1180,
            'text_width': 300,
            'output_path': 'output.pdf',
            'incremental': True
        },
    ]

    add_centered_text(contexts)


    contexts = [
        {
        'image_path': f"media/{first_image}",
        'file_name': 'output.pdf',
        'page_num': 8,
        'coordinates': (157, 283),
        'coef': 0.623,
        'output_path': 'output.pdf',
        'incremental': True
        },
        {
        'image_path': f"media/{second_image}",
        'file_name': 'output.pdf',
        'page_num': 10,
        'coordinates': (80, 287),
        'coef': 0.635,
        'output_path': 'output.pdf',
        'incremental': True
        },
    ]


    insert_images(contexts)

    context = {
            'file_name': 'output.pdf',
            'page_num': 6,
            'font_size': 92,
            'font_path': 'fonts/CodePro/Code-Pro.ttf',
            'text': niche,
            'color': (1, 1, 1),
            'y_coordinate': 430,
            'margin': 40,
            'output_path': 'output.pdf',
            'incremental': True
        }

    add_title(context)

    context = {
        # 'value_1': 300100000,
        # 'value_2': 25000000,
        # 'value_1': 250000,
        # 'value_2': 5001000,
        # 'value_1': 5643,
        # 'value_2': 10745,
        # 'value_1': 5,
        # 'value_2': 1000,
        # 'value_1': 5000,
        # 'value_2': 100,
        'value_1': int(views_search),
        'value_2': int(views_recommendations),
        'font_size': 30
        }

    create_diagram_page_8(context)

    context_page_10 = {
        'search_view_cost': cost_per_view_search,
        'search_contact_conversion_rate': conversion_rate_search,
        'search_contact_cost': cost_per_contact_search,
        'recommendation_view_cost': cost_per_view_recommendations,
        'recommendation_contact_conversion_rate': conversion_rate_recommendations,
        'recommendation_contact_cost': cost_per_contact_recommendations
    }

    create_diagram_page_10(context_page_10)

    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)

    filename = f"Презентация_{niche}_{moscow_time.strftime('%d%m%Y_%H%M')}.pdf"

    contexts = [
        {
            'file_name': 'output.pdf',
            'page_num': 9,
            'font_size': 33,
            'font_path': 'fonts/CodePro/Code-Pro-Bold.ttf',
            'text': '',
            'color': (184 / 255, 1, 0),
            'coordinates': (390, 360),
            'output_path': filename,
            'incremental': False
        },
    ]

    insert_texts(contexts)

    return os.path.join(settings.BASE_DIR, f"CreatePresentation/{filename}"), filename

import os

pdf_file = "output.pdf"
page_number = 10
acrobat_path = fr"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
# Команда для открытия PDF в Adobe Acrobat на нужной странице
# os.system(f'start "" "{acrobat_path}" /A "page={page_number}" "{pdf_file}"')