from django.db import models
from django.utils import timezone

from profil.models import Profil


class Anketa(models.Model):

    naziv = models.CharField(max_length=200)
    opis = models.TextField(blank=True)
    profil = models.ManyToManyField(
        Profil, blank=True, through='AnketaPopunjena')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.naziv


class AnketaPitanje(models.Model):
    anketa = models.ForeignKey(Anketa, on_delete=models.CASCADE)
    pitanje_text = models.CharField(max_length=200)
    opcija_one = models.CharField(max_length=30)
    opcija_two = models.CharField(max_length=30)
    opcija_three = models.CharField(max_length=30)
    opcija_one_count = models.IntegerField(default=0)
    opcija_two_count = models.IntegerField(default=0)
    opcija_three_count = models.IntegerField(default=0)

    def __str__(self):
        return self.pitanje_text


class AnketaPopunjena(models.Model):
    anketa = models.ForeignKey(Anketa, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    popunjena_anketa = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.anketa}+{self.popunjena_anketa}+{self.profil}'
