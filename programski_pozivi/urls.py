from django.urls import path
from . import views

app_name = 'programski_pozivi'

urlpatterns = [
    path('', views.kreiraj_programski_poziv, name='kreiranje_poziva'),
    path('<int:pk>/', views.kreiraj_pitanja_programski_poziv, name='kreiranje_pitanja'),
]
