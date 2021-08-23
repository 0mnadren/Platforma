from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

from profil.models import Profil, Oblast

# nemanja zivkovic
class Obavestenje(models.Model):
    profil = models.ManyToManyField(Profil)

    naslov = models.CharField(max_length=60, unique=True)
    tekst = models.TextField()
    datum_vreme_kreiranja = models.DateTimeField(auto_now_add=True)
    potpis = models.CharField(max_length=60)  # Mozda treba ImageField?

    def __str__(self):
        return self.naslov


class Rad(models.Model):
    oblasti = models.ManyToManyField(Oblast)

    profil = models.ManyToManyField(
        Profil,
        through='ProsledjenRad'
    )

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

    kada_poslat = models.DateField()
    konacna_odluka = models.BooleanField()

    def __str__(self):
        return f"Rad {self.rad} prosledjen {self.kada_poslat} {self.profil}"


### ANKETE vukasin ###
class Anketa(models.Model):

    ### Treba da se doda relationship
    oblasti = models.ManyToManyField(Oblast)

    # edit profile 
    # profil = models.ManyToManyField(Profil)
    naziv = models.CharField(max_length=125, unique=True)
    opis = models.TextField(blank=True)

    def __str__(self):
        return self.naziv

RATING_CHOICES = ((0, "Slazem se"), (1, "Ne slazem se"), (2, "Ne znam"),)

class AnketaPitanje(models.Model):
    anketa = models.ForeignKey(Anketa, on_delete=models.CASCADE)

    pitanje = models.CharField(max_length=225)

    ### Ponudjeni odgovori??? ###
    odgovor = models.TextField(blank=True)
    ponudjeni_odgovor = models.SmallIntegerField(choices=RATING_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.pitanje


### PROGRAMSKI POZIV ###
class ProgramskiPoziv(models.Model):
    oblast = models.OneToOneField(Oblast, on_delete=models.CASCADE) # profa rekao ne treba

    rad = models.ManyToManyField(Rad) # mozda moze da se odradi preko oblast

    konacna_ocena = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        blank=True, null=True,
    )

    def __str__(self):
        return f"Programski poziv iz oblasti {self.oblast}"


class ProgramskiPozivPitanje(models.Model):
    programski_poziv = models.ForeignKey(ProgramskiPoziv, on_delete=models.CASCADE)

    pitanje = models.CharField(max_length=225)
    odgovor = models.TextField(blank=True,)

    def __str__(self):
        return self.pitanje


