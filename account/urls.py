from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


from django.conf.urls.static import static
from django.conf import settings

app_name = 'account'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('status/', views.status, name='status'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
