from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('kdramas/', views.kdramas_index, name='index'),
  path('kdramas/<int:kdrama_id>/', views.kdrama_detail, name='detail'),
  path('kdramas/create/', views.KdramaCreate.as_view(), name='kdrama_create'),
  path('kdramas/<int:pk>/update/', views.KdramaUpdate.as_view(), name='kdrama_update'),
  path('kdramas/<int:pk>/delete/', views.KdramaDelete.as_view(), name='kdrama_delete'),
  path('kdramas/<int:kdrama_id>/add_watching/', views.add_watching, name='add_watching'),
  path('kdramas/<int:kdrama_id>/add_photo/', views.add_photo, name='add_photo'),
  path('kdramas/<int:kdrama_id>/assoc_award/<int:award_id>/', views.assoc_award, name='assoc_award'),
  path('kdramas/<int:kdrama_id>/disassoc_award/<int:award_id>/', views.disassoc_award, name='disassoc_award'),
  path('awards/', views.AwardList.as_view(), name='awards_index'),
  path('awards/<int:pk>/', views.AwardDetail.as_view(), name='award_detail'),
  path('awards/create/', views.AwardCreate.as_view(), name='award_create'),
  path('awards/<int:pk>/update/', views.AwardUpdate.as_view(), name='award_update'),
  path('awards/<int:pk>/delete/', views.AwardDelete.as_view(), name='award_delete'),
]