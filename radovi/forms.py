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
            'datum_podnosenja',
            'godina',
            'opis',
            'biografije',
        ]
        labels = {
            'clanovi': 'Članovi',
        }

    def clean_programski_poziv(self):
        data = self.cleaned_data['programski_poziv']
        try:
            if data.programskipozivpitanja:
                return data
        except AttributeError as e:
            raise forms.ValidationError('Ovaj programski poziv nema pitanja!')
        except data.programskipozivpitanja.DoesNotExist as e:
            raise forms.ValidationError('Ovaj programski poziv nema pitanja!')
