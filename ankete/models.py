from django.db import models

from profil.models import Oblast


### ANKETE ###
class Anketa(models.Model):

    ### Treba da se doda relationship
    oblasti = models.ManyToManyField(Oblast)

    naziv = models.CharField(max_length=125, unique=True)
    opis = models.TextField(blank=True)

    def __str__(self):
        return self.naziv


RATING_CHOICES = ((0, u"Slazem se"), (1, u"Ne slazem se"), (2, u"Ne znam"),)
class AnketaPitanje(models.Model):
    anketa = models.ForeignKey(Anketa, on_delete=models.CASCADE)

    pitanje = models.CharField(max_length=225)

    ### Ponudjeni odgovori??? ###
    odgovor = models.TextField(blank=True)
    ponudjeni_odgovor = models.SmallIntegerField(choices=RATING_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.pitanje
