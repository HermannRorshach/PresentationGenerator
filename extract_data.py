import pandas as pd

# Загрузка Excel файла
file_path = 'Первичный анализ ниши 9-13 Для презентации.xlsx'
xls = pd.ExcelFile(file_path)

# Извлечение данных с листа "Для разработчика" без заголовков
presentation_data = pd.read_excel(xls, sheet_name="Для разработчика", header=None)

# Устанавливаем первый столбец как индекс
presentation_data.set_index(0, inplace=True)

# Присваиваем значения переменным, используя индексы
views_search = presentation_data.loc["Просмотры в поисковой выдаче"].values[0]
views_recommendations = presentation_data.loc["Просмотры в рекомендациях"].values[0]
cost_per_view_search = presentation_data.loc["Цена просмотра в поисковой выдачи"].values[0]
cost_per_view_recommendations = presentation_data.loc["Цена просмотра в рекомендациях"].values[0]
conversion_rate_search = presentation_data.loc["Конверсия в контакт в поисковой выдаче"].values[0]
conversion_rate_recommendations = presentation_data.loc["Конверсия в контакт в рекомендациях"].values[0]
cost_per_contact_search = presentation_data.loc["Цена контакта в поисковой выдаче"].values[0]
cost_per_contact_recommendations = presentation_data.loc["Цена контакта в рекомендациях"].values[0]
optimal_ad_budget = presentation_data.loc["Оптимальный рекламный бюджет"].values[0]
total_contacts = presentation_data.loc["Количество контактов"].values[0]
average_contact_cost = presentation_data.loc["Средняя стоимость контакта"].values[0]
ad_publication_cost = presentation_data.loc["Публикация объявлений"].values[0]
ad_promotion_range = presentation_data.loc["Продвижение объявлений"].values[0]
budget_views_ads = presentation_data.loc["Бюджет на просмотры/объявления"].values[0]
budget_promotion_services = presentation_data.loc["Бюджет на услуги продвижения"].values[0]
avito_tariff_budget = presentation_data.loc["Бюджет на тариф авито"].values[0]
agency_service_cost = presentation_data.loc["Стоимость услуг агентства"].values[0]
tariff_name = presentation_data.loc["Название тарифа"].values[0]
total_ad_budget = presentation_data.loc["Суммарный рекламный бюджет"].values[0]
niche = presentation_data.loc["Ниша"].values[0]

# Проверка значений
print("Ниша:", niche)
print("Просмотры в поисковой выдаче:", views_search)
print("Суммарный рекламный бюджет:", total_ad_budget)
