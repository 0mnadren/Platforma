from django.urls import path
from . import views

app_name = 'administrator'

urlpatterns = [
    path('', views.profil, name='profil'),
    path('pregled_prijava', views.pregled_prijava, name='pregled_prijava'),
    path('pregled_prijava/<int:pk>/', views.prijava_detaljno, name='prijava_detaljno'),
    path('pregled_prijava/<int:pk>/prihvacena', views.prijava_prihvacena, name='prijava_prihvacena'),
    path('pregled_prijava/<int:pk>/odbijena', views.prijava_odbijena, name='prijava_odbijena'),
    path('kreiraj_obavestenje/', views.kreiraj_obavestenje, name='kreiraj_obavestenje'),
]
