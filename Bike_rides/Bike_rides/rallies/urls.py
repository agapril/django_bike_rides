from django.urls import path
from . import views


app_name = 'rallies'


urlpatterns = [
    path('', views.intro),
    path('home/', views.intro, name='home'),
    path('list/', views.RallyList.as_view(), name='list'),
    path('create/', views.RallyCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.RallyUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.RallyDelete.as_view(), name='delete'),
    path('detail/<int:pk>', views.RallyDetail.as_view(), name='detail'),
    path('register/', views.RallyRegisterView.as_view(), name='rally_register'),
    path('confirmed/<pk>', views.RallyConfirmedDetail.as_view(), name='rally_confirmed'),
]