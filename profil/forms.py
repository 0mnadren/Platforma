from django import forms
from .models import Profil
from django.utils.translation import gettext_lazy as _


class ProfilForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['biografija'].widget.initial_text = _("Trenutno")
        self.fields['biografija'].widget.input_text = _("Izaberi")

    class Meta:
        model = Profil
        fields = [
            'oblasti',
            'ime',
            'prezime',
            'nacionalnost',
            'NIO',
            'naucno_zvanje',
            'angazovanje',
            'adresa',
            'broj_telefona',
            'website',
            'biografija',
            'naucni_rad_1',
            'naucni_rad_2',
            'naucni_rad_3',
            'naucni_rad_4',
            'naucni_rad_5',
            'naucni_rad_6',
            'naucni_rad_7',
            'naucni_rad_8',
            'naucni_rad_9',
            'naucni_rad_10',
        ]
        labels = {
            'oblasti': _('Oblasti'),
            'ime': _('Ime'),
            'prezime': _('Prezime'),
            'nacionalnost': _('Nacionalnost'),
            'NIO': _('NIO (naučno istraživačka organizacija)'),
            'naucno_zvanje': _('Naučno zvanje'),
            'angazovanje': _('Angažovanje'),
            'adresa': _('Adresa'),
            'broj_telefona': _('Broj telefona',),
            'website': _('Lična veb stranica'),
            'biografija': _('biografija'),
            'naucni_rad_1': _('Naučni rad 1'),
            'naucni_rad_2': _('Naučni rad 2'),
            'naucni_rad_3': _('Naučni rad 3'),
            'naucni_rad_4': _('Naučni rad 4'),
            'naucni_rad_5': _('Naučni rad 5'),
            'naucni_rad_6': _('Naučni rad 6'),
            'naucni_rad_7': _('Naučni rad 7'),
            'naucni_rad_8': _('Naučni rad 8'),
            'naucni_rad_9': _('Naučni rad 9'),
            'naucni_rad_10': _('Naučni rad 10'),
        }

    
        # widgets = {
        #     'oblasti': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        #     'ime': forms.CharField(attrs={'class': 'form-control'}),
        #     'prezime': forms.CharField(attrs={'class': 'form-control'}),
        #     'nacionalnost': forms.CharField(attrs={'class': 'form-control'}),
        #     'NIO': forms.CharField(attrs={'class': 'form-control'}),
        #     'naucno_zvanje': forms.CharField(attrs={'class': 'form-control'}),
        #     'angazovanje': forms.CharField(attrs={'class': 'form-control'}),
        #     'adresa': forms.CharField(attrs={'class': 'form-control'}),
        #     'broj_telefona': forms.CharField(attrs={'class': 'form-control'}),
        #     'website': forms.URLField(),
        #     'biografija': forms.FileField(attrs={'class': 'form-control'}),
        #     'naucni_rad_1': forms.CharField(attrs={'class': 'form-control'}),
        #     'naucni_rad_2': forms.CharField(attrs={'class': 'form-control'}),
        #     'naucni_rad_3': forms.CharField(attrs={'class': 'form-control'}),
        #     'naucni_rad_4': forms.CharField(attrs={'class': 'form-control'}),
        #     'naucni_rad_5': forms.CharField(attrs={'class': 'form-control'}),
        #     'naucni_rad_6': forms.CharField(attrs={'class': 'form-control'}),
        #     'naucni_rad_7': forms.CharField(attrs={'class': 'form-control'}),
        #     'naucni_rad_8': forms.CharField(attrs={'class': 'form-control'}),
        #     'naucni_rad_9': forms.CharField(attrs={'class': 'form-control'}),
        #     'naucni_rad_10': forms.CharField(attrs={'class': 'form-control dark'}),
        # }
