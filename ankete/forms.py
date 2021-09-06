from django import forms
from . models import Anketa, AnketaPitanje


class CreateAnketaForm(forms.ModelForm):
    class Meta:
        model = Anketa
        # fields = '__all__'
        fields = ['naziv', 'opis']


class CreateAnketaPitanjeForm(forms.ModelForm):
    class Meta:
        model = AnketaPitanje
        fields = ['pitanje_text', 'opcija_one',
                  'opcija_two', 'opcija_three']
