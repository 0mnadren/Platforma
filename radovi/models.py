from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

from profil.models import Oblast, Profil
from programski_pozivi.models import ProgramskiPoziv


class Rad(models.Model):
    oblasti = models.ManyToManyField(Oblast)

    profil = models.ManyToManyField(
        Profil,
        through='ProsledjenRad'
    )

    programski_poziv = models.ForeignKey(ProgramskiPoziv, on_delete=models.CASCADE)

    naziv = models.CharField(max_length=125, unique=True)
    kategorija = models.CharField(max_length=60)
    opis = models.TextField()
    clanovi = models.CharField(max_length=225)

    godina = models.PositiveIntegerField(
        validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.now().year)],
        help_text="Use the following format: YYYY")

    ### Da li ovde treba da budu File Fields ###
    # Za opis, spisak clanova, godina i biografija clanova
    biografije = models.TextField()

    datum_podnosenja = models.DateField()

    """
    Proveri kako da se spoje u jedan File i ubace direktno u FileField
        dokument = metoda(datum_podnosenja, biografija)
        file = models.FileField()
    """

    def __str__(self):
        return f"Naziv: {self.naziv} -- Kategorija: {self.kategorija}"


class ProsledjenRad(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    rad = models.ForeignKey(Rad, on_delete=models.CASCADE)

    kada_poslat = models.DateField(auto_now_add=True)
    konacna_odluka = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"Rad {self.rad} prosledjen {self.kada_poslat} {self.profil}"

