from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def upload_files(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        images = request.FILES.getlist('images')

        # Сохраняем файлы
        fs = FileSystemStorage()
        excel_filename = fs.save(excel_file.name, excel_file)
        image_filenames = [fs.save(image.name, image) for image in images]

        # Дальнейшая обработка файлов

    return render(request, 'CreatePresentation/upload_files.html')
