from django import forms
from django.utils.translation import gettext_lazy as _

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
            'naziv': _('Naziv'),
            'kategorija': _('Kategorija'),
            'oblasti': _('Oblasti'),
            'programski_poziv': _('Programski poziv'),
            'clanovi': _('Članovi'),
            'datum_podnosenja': _('Datum podnošenja'),
            'godina': _('Godina'),
            'opis': _('Opis'),
            'biografije': _('Biografije'),
        }

    def clean_programski_poziv(self):
        data = self.cleaned_data['programski_poziv']
        try:
            if data.programskipozivpitanja:
                return data
        except AttributeError as e:
            raise forms.ValidationError(_('Ovaj programski poziv nema pitanja!'))
        except data.programskipozivpitanja.DoesNotExist as e:
            raise forms.ValidationError(_('Ovaj programski poziv nema pitanja!'))
