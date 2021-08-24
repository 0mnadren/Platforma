from django.urls import path
from . import views

app_name = 'profil'

urlpatterns = [
    path('', views.profil, name='profil'),
    path('prijava/', views.prijava, name='prijava'),
    path('ankete/', views.ankete, name='ankete'),
]
