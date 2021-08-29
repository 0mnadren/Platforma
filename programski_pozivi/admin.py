from django.contrib import admin
from .models import \
    ProgramskiPoziv, \
    ProgramskiPozivPitanja, \
    ProgramskiPozivOdgovori

admin.site.register(ProgramskiPoziv)
admin.site.register(ProgramskiPozivPitanja)
admin.site.register(ProgramskiPozivOdgovori)
