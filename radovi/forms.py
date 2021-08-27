from django import forms

from .models import Rad


class RadForm(forms.ModelForm):

    class Meta:
        model = Rad
        fields = [
            'naziv',
            'kategorija',
            'oblasti',
            'programski_poziv',
            'clanovi',
            'godina',
            'opis',
            'biografije',
            'datum_podnosenja',
        ]
