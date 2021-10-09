from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Obavestenje
from profil.models import Oblast


class ObavestenjeForm(forms.ModelForm):
    class Meta:
        model = Obavestenje
        fields = [
            'profil',
            'naslov',
            'tekst',
            'potpis',
        ]

        labels = {
            'profil': _('Profil'),
            'naslov': _('Naslov'),
            'tekst': _('Tekst'),
            'potpis': _('Potpis'),
        }

        widgets = {
            'profil': forms.SelectMultiple(attrs={'id': 'myselect'})
        }
    

class OblastForm(forms.ModelForm):
    class Meta:
        model = Oblast
        fields = ['naziv']
        labels = {
            'naziv': _('Naziv'),
        }
