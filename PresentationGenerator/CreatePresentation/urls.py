from django.urls import path

from . import views


app_name = 'CreatePresentation'

urlpatterns = [
    path('', views.upload_files, name='upload_files'),
#     path('upload-sample', views.UploadSample.as_view(), name='upload_sample'),
#     path('process-template/<int:pk>/', views.ProcessTemplateView.as_view(), name='process_template'),
#
]
