from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


UserAdmin.list_display += ('profile_accepted',)

admin.site.register(User, UserAdmin)
