from django.db import models

from profil.models import Profil


class Obavestenje(models.Model):
    profil = models.ManyToManyField(Profil)

    naslov = models.CharField(max_length=60)
    tekst = models.TextField()
    datum_vreme_kreiranja = models.DateTimeField(auto_now_add=True)
    potpis = models.CharField(max_length=60)

    def __str__(self):
        return self.naslov

