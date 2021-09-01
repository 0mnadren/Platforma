from django.urls import path
from . import views

app_name = 'profil'

urlpatterns = [
    path('', views.profil, name='profil'),
    path('search/', views.search, name='search'),
    path('<int:pk>/obrisi/', views.obrisi_obavestenje, name='obrisi_obavestenje'),
    path('prijava/', views.prijava, name='prijava'),
]
