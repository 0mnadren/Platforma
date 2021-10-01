from django.contrib import admin
from .models import Oblast, Profil


class ProfilAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'ime', 'prezime', 'naucno_zvanje', 'pregledane_ankete'
    ]


admin.site.register(Oblast)
admin.site.register(Profil, ProfilAdmin)
