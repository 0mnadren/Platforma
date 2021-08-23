from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from profil.models import Oblast


### PROGRAMSKI POZIV ###
class ProgramskiPoziv(models.Model):
    oblast = models.OneToOneField(Oblast, on_delete=models.CASCADE)

    # rad = models.ManyToManyField(Rad) mozda moze da se odradi preko oblast

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
