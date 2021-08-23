from django.contrib import admin
from .models import (
    Obavestenje,
    Rad,
    ProsledjenRad,
    Anketa,
    AnketaPitanje,
    ProgramskiPoziv,
    ProgramskiPozivPitanje,
    ProgramskiPozivOdgovor,
)

admin.site.register(Obavestenje)
admin.site.register(Rad)
admin.site.register(ProsledjenRad)
admin.site.register(Anketa)
admin.site.register(AnketaPitanje)
admin.site.register(ProgramskiPoziv)
admin.site.register(ProgramskiPozivPitanje)
admin.site.register(ProgramskiPozivOdgovor)

