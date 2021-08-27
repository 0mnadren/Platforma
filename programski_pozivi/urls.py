from django.urls import path
from . import views

app_name = 'programski_pozivi'

urlpatterns = [
    path('', views.kreiraj_programski_poziv, name='kreiraj_programski_poziv'),
    path('<int:pk>/azuriraj/', views.azuriraj_programski_poziv, name='azuriraj_programski_poziv'),
    path('<int:pk>/detaljno/', views.detaljno_programski_poziv, name='detaljno_programski_poziv'),
    path('<int:pk>/obrisi/', views.obrisi_programski_poziv, name='obrisi_programski_poziv'),

    path('kreiranje_pitanja/<int:pk>/', views.kreiraj_pitanja_programski_poziv, name='kreiraj_pitanja'),
    path('detaljno_pitanja/<int:pk>/', views.detaljno_pitanja_programski_poziv, name='detaljno_pitanja'),
]
