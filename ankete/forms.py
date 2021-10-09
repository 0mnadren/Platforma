from django import forms
from django.utils.translation import gettext_lazy as _
from . models import Anketa, AnketaPitanje


class CreateAnketaForm(forms.ModelForm):
    class Meta:
        model = Anketa
        fields = ['naziv', 'opis']
        labels = {
            'naziv': _('Naziv'),
            'opis': _('Opis'),
        }


class CreateAnketaPitanjeForm(forms.ModelForm):
    class Meta:
        model = AnketaPitanje
        fields = ['pitanje_text', 'opcija_one',
                  'opcija_two', 'opcija_three']
        labels = {
            'pitanje_text': _('Pitanje tekst'),
            'opcija_one': _('Opcija jedan'),
            'opcija_two': _('Opcija dva'),
            'opcija_three': _('Opcija tri'),
        }
