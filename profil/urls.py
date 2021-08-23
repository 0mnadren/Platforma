from django.urls import path
from . import views

app_name = 'profil'

urlpatterns = [
    path('', views.profil, name='profil'),
    path('prijava/', views.prijava, name='prijava'),

    path('lista_radova/', views.lista_radova, name='lista_radova'),
    path('lista_radova/<int:pk>/', views.naucni_rad, name='naucni_rad'),
]
