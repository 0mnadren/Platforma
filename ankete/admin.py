from django.contrib import admin
from .models import \
    Anketa, \
    AnketaPitanje,\
    AnketaPopunjena


class AnketaPitanjeAdmin(admin.TabularInline):
    model = AnketaPitanje


class AnketaAdmin(admin.ModelAdmin):
    inlines = [AnketaPitanjeAdmin, ]


admin.site.register(Anketa, AnketaAdmin)
admin.site.register(AnketaPopunjena)
