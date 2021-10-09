from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


UserAdmin.list_display = ('username', 'email', 'is_staff', 'profile_accepted', 'last_login', 'date_joined')

admin.site.register(User, UserAdmin)
admin.site.site_header = _('Portal za ocenjivanje naučnih radova Django Admin')
