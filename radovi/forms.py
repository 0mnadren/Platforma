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

    def clean_programski_poziv(self):
        data = self.cleaned_data['programski_poziv']
        try:
            if data.programskipozivpitanja:
                return data
        except AttributeError as e:
            raise forms.ValidationError('Ovaj programski poziv nema pitanja!')
        except data.programskipozivpitanja.DoesNotExist as e:
            raise forms.ValidationError('Ovaj programski poziv nema pitanja!')
