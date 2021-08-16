from django import forms
from .models import Profil


class ProfilForm(forms.ModelForm):

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
