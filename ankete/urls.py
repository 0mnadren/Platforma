from django.urls import path
from . import views

app_name = 'ankete'
urlpatterns = [
    path('', views.ankete, name='ankete'),
]