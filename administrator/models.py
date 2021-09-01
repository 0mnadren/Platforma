from django.db import models
from django.db.models.base import Model

from profil.models import Profil


class Obavestenje(models.Model):
    profil = models.ManyToManyField(Profil, through='ObrisanoStanje')

    naslov = models.CharField(max_length=60)
    tekst = models.TextField()
    datum_vreme_kreiranja = models.DateTimeField(auto_now_add=True)
    potpis = models.CharField(max_length=60)


    def __str__(self):
        return self.naslov
    
class Obrisanostanje(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='korisnik')
    obavestenje = models.ForeignKey(Obavestenje, on_delete=models.CASCADE, related_name='obavest')
    obrisano = models.BooleanField(default=False)
    

    def __str__(self):
        return f'{self.profil} + {self.obrisano}'