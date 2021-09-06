from django.urls import path
from . import views

app_name = 'ankete'
urlpatterns = [
    # admin
    path('admin_ankete/', views.admin_ankete, name='admin_ankete'),
    path('create_anketa/', views.create_anketa, name='create_anketa'),
    path('delete_anketa/<int:pk>', views.delete_anketa, name='delete_anketa'),
    path('rezultat_anketa/<int:pk>', views.rezultat_anketa, name='rezultat_anketa'),
    path('posalji_anketa/<int:pk>', views.posalji_anketa, name='posalji_anketa'),
    path('glasaj_anketa/<int:pk>', views.glasaj_anketa, name='glasaj_anketa'),
    path('ignorisi_anketa/<int:pk>', views.ignorisi_anketa, name='ignorisi_anketa'),
    path('create_pitanje/<int:pk>', views.create_pitanje, name='create_pitanje'),

    # profil
    path('', views.ankete, name='ankete'),
    path('rezultat_anketa_profil/<int:pk>',
         views.rezultat_anketa_profil, name='rezultat_anketa_profil')
]
