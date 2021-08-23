from django import forms

from .models import ProgramskiPoziv, ProgramskiPozivOdgovor


class ProgramskiPozivForm(forms.ModelForm):
    class Meta:
        model = ProgramskiPoziv
        fields = ['naziv']


class ProgramskiPozivOdgovorForm(forms.ModelForm):
    class Meta:
        model = ProgramskiPozivOdgovor
        fields = ['odgovor']


