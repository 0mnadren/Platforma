from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

from profil.models import Oblast, Profil
from profil.validators import validate_file_extension
from programski_pozivi.models import ProgramskiPoziv


class Rad(models.Model):
    oblasti = models.ManyToManyField(Oblast)

    profil = models.ManyToManyField(
        Profil,
        through='ProsledjenRad'
    )

    programski_poziv = models.ForeignKey(ProgramskiPoziv, on_delete=models.CASCADE)

    naziv = models.CharField(max_length=225, unique=True)
    kategorija = models.CharField(max_length=125)
    clanovi = models.CharField(max_length=225)
    godina = models.PositiveIntegerField(
        validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.now().year)],
        help_text="Koristi sledeći format: GGGG")

    opis = models.FileField(upload_to='radovi/opis/pdfs', validators=[validate_file_extension])
    biografije = models.FileField(upload_to='radovi/biografije/pdfs', validators=[validate_file_extension])

    datum_podnosenja = models.DateField(help_text='Koristi sledeći format: GGGG-MM-DD')

    prihvacen_rad = models.BooleanField(default=None, null=True)

    def __str__(self):
        return f"Naziv: {self.naziv} -- Kategorija: {self.kategorija}"


class ProsledjenRad(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    rad = models.ForeignKey(Rad, on_delete=models.CASCADE)

    kada_poslat = models.DateField(auto_now_add=True)

    zakljucani_odgovori = models.BooleanField(default=False)

    def __str__(self):
        return f"Rad {self.rad} prosledjen je {self.kada_poslat} | {self.profil}"

