from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . main import extract_data, main
import os
from django.conf import settings
from django.http import FileResponse, HttpResponse
from io import BytesIO
import shutil


def remove_garbage(folder_path):
    # Удаление файлов по условиям
    for filename in os.listdir(folder_path):
        if filename.startswith('Презентация') and filename.endswith('.pdf') or filename == 'output.pdf':
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)  # Удаление файла

    # Удаление всех файлов в папке media
    media_folder_path = os.path.join(settings.MEDIA_ROOT)  # Убедитесь, что settings импортированы
    for media_filename in os.listdir(media_folder_path):
        media_file_path = os.path.join(media_folder_path, media_filename)
        if os.path.isfile(media_file_path):  # Проверяем, является ли это файлом
            os.remove(media_file_path)  # Удаление файла
        elif os.path.isdir(media_file_path):  # Если это директория, удаляем ее и все содержимое
            shutil.rmtree(media_file_path)


def upload_files(request):
    remove_garbage(os.path.join(settings.BASE_DIR, "CreatePresentation"))

    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        images = request.FILES.getlist('images')

        # Сохраняем файлы
        fs = FileSystemStorage()
        excel_filename = fs.save(excel_file.name, excel_file)  # Сохраненное имя Excel файла
        saved_image_filenames = [fs.save(image.name, image) for image in images]  # Сохраненные имена изображений
        first_image, second_image = saved_image_filenames

        # Дальнейшая обработка файлов
        all_data = extract_data(os.path.join(settings.MEDIA_ROOT, excel_filename))
        pdf_file_path, filename = main(all_data, first_image, second_image)

        # Удаляем загруженные файлы
        fs.delete(excel_filename)
        fs.delete(first_image)
        fs.delete(second_image)

        # Создание выходного потока
        pdf_output_stream = BytesIO()

        # Путь к уже существующему PDF-файлу
        existing_pdf_path = pdf_file_path

        # Открытие и копирование содержимого
        with open(existing_pdf_path, 'rb') as existing_pdf_file:
            pdf_output_stream.write(existing_pdf_file.read())

        # Переместить указатель потока в начало
        pdf_output_stream.seek(0)
        return FileResponse(pdf_output_stream, as_attachment=True, filename=f"{filename}.pdf")


    return render(request, 'CreatePresentation/upload_files.html')

def faq(request):
    return render(request, 'CreatePresentation/FAQ.html')

def contacts(request):
    return render(request, 'CreatePresentation/contacts.html')
