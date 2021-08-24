from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from profil.models import Profil


### PROGRAMSKI POZIV ###
class ProgramskiPoziv(models.Model):

    naziv = models.CharField(max_length=125)
    konacna_ocena = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        blank=True, null=True,
    )

    def __str__(self):
        return f"{self.naziv}"


class ProgramskiPozivPitanje(models.Model):
    programski_poziv = models.ForeignKey(ProgramskiPoziv, on_delete=models.CASCADE)

    pitanje = models.CharField(max_length=225)

    def __str__(self):
        return self.pitanje


class ProgramskiPozivOdgovor(models.Model):
    pitanje = models.ManyToManyField(ProgramskiPozivPitanje)

    profil = models.ManyToManyField(Profil)

    odgovor = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True, null=True,
    )

    def __str__(self):
        return f'Profil na pitanje odgovor {self.odgovor}'
