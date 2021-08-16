from django.db import models
from django.conf import settings

from .validators import validate_file_extension, phone_regex


class Oblast(models.Model):
    naziv = models.CharField(max_length=125, unique=True)

    def __str__(self):
        return self.naziv


class Profil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    oblasti = models.ManyToManyField(Oblast)

    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=30)
    nacionalnost = models.CharField(max_length=30)
    NIO = models.CharField(max_length=125)
    naucno_zvanje = models.CharField(verbose_name='naucno zvanje', max_length=125)
    angazovanje = models.CharField(max_length=125)
    adresa = models.CharField(max_length=125)

    broj_telefona = models.CharField(validators=[phone_regex], max_length=17)

    website = models.URLField(max_length=225, blank=True, null=True)

    biografija = models.FileField(upload_to='profil/pdfs', validators=[validate_file_extension]) # Ovde nedostaje upload_to

    naucni_rad_1 = models.CharField(max_length=125)
    naucni_rad_2 = models.CharField(max_length=125)
    naucni_rad_3 = models.CharField(max_length=125)
    naucni_rad_4 = models.CharField(max_length=125)
    naucni_rad_5 = models.CharField(max_length=125)
    naucni_rad_6 = models.CharField(max_length=125)
    naucni_rad_7 = models.CharField(max_length=125)
    naucni_rad_8 = models.CharField(max_length=125)
    naucni_rad_9 = models.CharField(max_length=125)
    naucni_rad_10 = models.CharField(max_length=125)

    # STANJE_PRIJAVE
    pregleda_se = models.BooleanField(default=False)  # Da sluzi za pending kod administratora, otvori prijavu postane True?

    pregledane_ankete = models.IntegerField(verbose_name='broj pregledanih anketa', default=0)

    def __str__(self):
        return f"Korisnik: {self.user} -- Ime: {self.ime} {self.prezime}"
