from django import forms
from django.utils.translation import gettext_lazy as _

from .models import ProgramskiPoziv, ProgramskiPozivPitanja, ProgramskiPozivOdgovori


class ProgramskiPozivForm(forms.ModelForm):
    class Meta:
        model = ProgramskiPoziv
        fields = ['naziv', 'opis']
        labels = {
            'naziv': _('Naziv'),
            'opis': _('Opis'),
        }


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
        labels = {
            'pitanje1': _('Pitanje 1'),
            'pitanje2': _('Pitanje 2'),
            'pitanje3': _('Pitanje 3'),
            'pitanje4': _('Pitanje 4'),
            'pitanje5': _('Pitanje 5'),
            'pitanje6': _('Pitanje 6'),
            'pitanje7': _('Pitanje 7'),
            'pitanje8': _('Pitanje 8'),
            'pitanje9': _('Pitanje 9'),
            'pitanje10': _('Pitanje 10'),
        }


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
        labels = {
            'odgovor1': _('Odgovor 1'),
            'odgovor2': _('Odgovor 2'),
            'odgovor3': _('Odgovor 3'),
            'odgovor4': _('Odgovor 4'),
            'odgovor5': _('Odgovor 5'),
            'odgovor6': _('Odgovor 6'),
            'odgovor7': _('Odgovor 7'),
            'odgovor8': _('Odgovor 8'),
            'odgovor9': _('Odgovor 9'),
            'odgovor10': _('Odgovor 10'),
        }

    def clean_odgovor1(self):
        data = self.cleaned_data['odgovor1']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError(_('Ocena mora da bude od 1 do 10!'))

    def clean_odgovor2(self):
        data = self.cleaned_data['odgovor2']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError(_('Ocena mora da bude od 1 do 10!'))

    def clean_odgovor3(self):
        data = self.cleaned_data['odgovor3']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError(_('Ocena mora da bude od 1 do 10!'))

    def clean_odgovor4(self):
        data = self.cleaned_data['odgovor4']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError(_('Ocena mora da bude od 1 do 10!'))

    def clean_odgovor5(self):
        data = self.cleaned_data['odgovor5']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError(_('Ocena mora da bude od 1 do 10!'))

    def clean_odgovor6(self):
        data = self.cleaned_data['odgovor6']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError(_('Ocena mora da bude od 1 do 10!'))

    def clean_odgovor7(self):
        data = self.cleaned_data['odgovor7']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError(_('Ocena mora da bude od 1 do 10!'))

    def clean_odgovor8(self):
        data = self.cleaned_data['odgovor8']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError(_('Ocena mora da bude od 1 do 10!'))

    def clean_odgovor9(self):
        data = self.cleaned_data['odgovor9']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError(_('Ocena mora da bude od 1 do 10!'))

    def clean_odgovor10(self):
        data = self.cleaned_data['odgovor10']
        if 0 < data <= 10:
            return data
        raise forms.ValidationError(_('Ocena mora da bude od 1 do 10!'))


