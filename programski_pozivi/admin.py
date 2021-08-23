from django.contrib import admin
from .models import (
    ProgramskiPoziv,
    ProgramskiPozivPitanje
)

admin.site.register(ProgramskiPoziv)
admin.site.register(ProgramskiPozivPitanje)
