from django.contrib import admin

from .models import \
    Rad, \
    ProsledjenRad


class RadAdmin(admin.ModelAdmin):
    list_display = ['naziv', 'kategorija', 'programski_poziv', 'prihvacen_rad']


admin.site.register(Rad, RadAdmin)
admin.site.register(ProsledjenRad)
