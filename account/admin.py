from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


UserAdmin.list_display = ('username', 'email', 'is_staff', 'profile_accepted', 'last_login', 'date_joined')

admin.site.register(User, UserAdmin)
admin.site.site_header = 'Portal za ocenjivanje naučnih radova Django Admin'
