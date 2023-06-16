from django.urls import path
from . import views


app_name = 'rides'


urlpatterns = [
    path('upload/', views.UploadFileView.as_view(), name='upload_file'),
    path('file_uploaded/<pk>', views.FileUploadedSummary.as_view(), name='file_uploaded_summary'),
    path('list/', views.RidesListView.as_view(), name='list')
]