from django import forms
from django.forms import widgets
from .models import Obavestenje
from profil.models import Oblast


class ObavestenjeForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    # super().__init__(*args, **kwargs)
    # self.fields['biografija'].widget.initial_text = "currently"
    # self.fields['biografija'].widget.input_text = "NE DIRAJ"
    class Meta:
        model = Obavestenje
        fields = [
            'profil',
            'naslov',
            'tekst',
            'potpis',
        ]


class OblastForm(forms.ModelForm):
    class Meta:
        model = Oblast
        fields = ['naziv']
