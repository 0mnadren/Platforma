from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from profil.models import Profil


### PROGRAMSKI POZIV ###
class ProgramskiPoziv(models.Model):

    naziv = models.CharField(max_length=125)
    opis = models.TextField()

    def __str__(self):
        return f"{self.naziv}"


class ProgramskiPozivPitanja(models.Model):
    programski_poziv = models.OneToOneField(ProgramskiPoziv, on_delete=models.CASCADE)

    pitanje1 = models.CharField(max_length=225)
    pitanje2 = models.CharField(max_length=225)
    pitanje3 = models.CharField(max_length=225)
    pitanje4 = models.CharField(max_length=225)
    pitanje5 = models.CharField(max_length=225)
    pitanje6 = models.CharField(max_length=225)
    pitanje7 = models.CharField(max_length=225)
    pitanje8 = models.CharField(max_length=225)
    pitanje9 = models.CharField(max_length=225)
    pitanje10 = models.CharField(max_length=225)

    def __str__(self):
        return self.programski_poziv.naziv


class ProgramskiPozivOdgovori(models.Model):
    programski_poziv_pitanja = models.ForeignKey(ProgramskiPozivPitanja, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)

    odgovor1 = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True, null=True,
    )
    odgovor2 = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True, null=True,
    )
    odgovor3 = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True, null=True,
    )
    odgovor4 = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True, null=True,
    )
    odgovor5 = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True, null=True,
    )
    odgovor6 = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True, null=True,
    )
    odgovor7 = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True, null=True,
    )
    odgovor8 = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True, null=True,
    )
    odgovor9 = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True, null=True,
    )
    odgovor10 = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True, null=True,
    )

    ukupan_broj_poena = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        blank=True, default=0,
    )

    def izracunaj_ukupan_broj_poena(self):
        self.ukupan_broj_poena = 0
        self.ukupan_broj_poena += self.odgovor1
        self.ukupan_broj_poena += self.odgovor2
        self.ukupan_broj_poena += self.odgovor3
        self.ukupan_broj_poena += self.odgovor4
        self.ukupan_broj_poena += self.odgovor5
        self.ukupan_broj_poena += self.odgovor6
        self.ukupan_broj_poena += self.odgovor7
        self.ukupan_broj_poena += self.odgovor8
        self.ukupan_broj_poena += self.odgovor9
        self.ukupan_broj_poena += self.odgovor10

    def __str__(self):
        return f'{self.profil} programski poziv pitanja {self.programski_poziv_pitanja}'
