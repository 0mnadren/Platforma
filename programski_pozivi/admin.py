from django.contrib import admin
from .models import \
    ProgramskiPoziv, \
    ProgramskiPozivPitanja, \
    ProgramskiPozivOdgovori


class ProgramskiPozivPitanjaInline(admin.StackedInline):
    model = ProgramskiPozivPitanja


class ProgramskiPozivAdmin(admin.ModelAdmin):
    inlines = [ProgramskiPozivPitanjaInline]
    list_display = ['naziv', 'opis']
    search_fields = ['opis']


admin.site.register(ProgramskiPoziv, ProgramskiPozivAdmin)
admin.site.register(ProgramskiPozivOdgovori)
