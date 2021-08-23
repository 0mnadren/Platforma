from django.contrib import admin
from .models import (
    Anketa,
    AnketaPitanje,
)

admin.site.register(Anketa)
admin.site.register(AnketaPitanje)
