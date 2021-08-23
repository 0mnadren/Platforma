from django.urls import path
from . import views

app_name = 'administrator'

urlpatterns = [
    path('', views.profil, name='profil'),
    path('pregled_prijava/', views.pregled_prijava, name='prijave'),
    path('pregled_prijava/<int:pk>/', views.prijava_detaljno, name='prijava_detaljno'),
    path('pregled_prijava/<int:pk>/prihvacena/', views.prijava_prihvacena, name='prijava_prihvacena'),
    path('pregled_prijava/<int:pk>/odbijena/', views.prijava_odbijena, name='prijava_odbijena'),

    path('kreiraj_programski_poziv/', views.kreiraj_programski_poziv, name='kreiranje_poziva'),
    path('kreiraj_programski_poziv/<int:pk>/', views.kreiraj_pitanja_programski_poziv, name='kreiranje_pitanja'),
    path('naucni_radovi/', views.lista_naucnih_radova, name='naucni_radovi'),
    path('naucni_rad/<int:pk>/', views.naucni_rad, name='naucni_rad'),
]
