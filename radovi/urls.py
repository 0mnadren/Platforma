from django.urls import path
from . import views

app_name = 'radovi'

urlpatterns = [
    path('naucni_radovi_admin/', views.lista_radova_admin, name='lista_radova_admin'),
    path('naucni_rad_admin/<int:pk>/', views.naucni_rad_admin, name='naucni_rad_admin'),

    path('', views.lista_radova_profil, name='lista_radova_profil'),
    path('<int:pk>/', views.naucni_rad_profil, name='naucni_rad_profil'),
]
