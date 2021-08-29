from django.urls import path
from . import views

app_name = 'radovi'

urlpatterns = [
    path('radovi_admin_home/', views.radovi_admin_home, name='radovi_admin_home'),
    path('kreiraj_rad/', views.kreiraj_rad, name='kreiraj_rad'),
    path('lista_radova_admin/', views.lista_radova_admin, name='lista_radova_admin'),
    path('naucni_rad_admin/<int:pk>/', views.naucni_rad_admin, name='naucni_rad_admin'),
    path('konacna_odluka_rad_admin/<int:pk>/', views.konacna_odluka_rad_admin, name='konacna_odluka_rad_admin'),

    path('prosledjeni_radovi_admin/', views.prosledjeni_radovi_admin, name='prosledjeni_radovi_admin'),
    path('prosledjeni_radovi_admin/<int:pk>/oduzimanje', views.oduzimanje_rada_admin, name='oduzimanje_rada_admin'),


    path('', views.lista_radova_profil, name='lista_radova_profil'),
    path('<int:pk>/', views.naucni_rad_profil, name='naucni_rad_profil'),
]
