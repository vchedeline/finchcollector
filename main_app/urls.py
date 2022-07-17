from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('kdramas/', views.kdramas_index, name='index'),
  path('kdramas/<int:kdrama_id>/', views.kdrama_detail, name='detail'),
  path('kdramas/create/', views.KdramaCreate.as_view(), name='kdrama_create')
]