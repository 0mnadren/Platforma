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

    def clean_odgovor1(self):
        data = self.cleaned_data['odgovor1']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError('Ocena mora da bude od 1 do 10!')

    def clean_odgovor2(self):
        data = self.cleaned_data['odgovor2']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError('Ocena mora da bude od 1 do 10!')

    def clean_odgovor3(self):
        data = self.cleaned_data['odgovor3']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError('Ocena mora da bude od 1 do 10!')

    def clean_odgovor4(self):
        data = self.cleaned_data['odgovor4']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError('Ocena mora da bude od 1 do 10!')

    def clean_odgovor5(self):
        data = self.cleaned_data['odgovor5']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError('Ocena mora da bude od 1 do 10!')

    def clean_odgovor6(self):
        data = self.cleaned_data['odgovor6']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError('Ocena mora da bude od 1 do 10!')

    def clean_odgovor7(self):
        data = self.cleaned_data['odgovor7']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError('Ocena mora da bude od 1 do 10!')

    def clean_odgovor8(self):
        data = self.cleaned_data['odgovor8']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError('Ocena mora da bude od 1 do 10!')

    def clean_odgovor9(self):
        data = self.cleaned_data['odgovor9']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError('Ocena mora da bude od 1 do 10!')

    def clean_odgovor10(self):
        data = self.cleaned_data['odgovor10']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError('Ocena mora da bude od 1 do 10!')


