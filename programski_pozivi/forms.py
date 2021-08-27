from django import forms

from .models import ProgramskiPoziv, ProgramskiPozivPitanja, ProgramskiPozivOdgovori


class ProgramskiPozivForm(forms.ModelForm):
    class Meta:
        model = ProgramskiPoziv
        fields = ['naziv', 'opis']


class ProgramskiPozivPitanjaForm(forms.ModelForm):
    class Meta:
        model = ProgramskiPozivPitanja
        fields = [
            'pitanje1',
            'pitanje2',
            'pitanje3',
            'pitanje4',
            'pitanje5',
            'pitanje6',
            'pitanje7',
            'pitanje8',
            'pitanje9',
            'pitanje10',
        ]


class ProgramskiPozivOdgovoriForm(forms.ModelForm):
    class Meta:
        model = ProgramskiPozivOdgovori
        fields = [
            'odgovor1',
            'odgovor2',
            'odgovor3',
            'odgovor4',
            'odgovor5',
            'odgovor6',
            'odgovor7',
            'odgovor8',
            'odgovor9',
            'odgovor10',
        ]
