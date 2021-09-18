from django import forms
from .models import Profil


class ProfilForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['biografija'].widget.initial_text = "Trenutno"
        self.fields['biografija'].widget.input_text = "Izaberi"

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
            'NIO': 'NIO (naučno istraživačka organizacija)',
            'naucno_zvanje': 'Naucčno zvanje',
            'angazovanje': 'Angažovanje',
            'website': 'Lična veb stranica',
            'naucni_rad_1': 'Naučni rad 1',
            'naucni_rad_2': 'Naučni rad 2',
            'naucni_rad_3': 'Naučni rad 3',
            'naucni_rad_4': 'Naučni rad 4',
            'naucni_rad_5': 'Naučni rad 5',
            'naucni_rad_6': 'Naučni rad 6',
            'naucni_rad_7': 'Naučni rad 7',
            'naucni_rad_8': 'Naučni rad 8',
            'naucni_rad_9': 'Naučni rad 9',
            'naucni_rad_10': 'Naučni rad 10',
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
