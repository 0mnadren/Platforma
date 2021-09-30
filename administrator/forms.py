from django import forms
from django.db.models.fields import Field
from django.forms import widgets
from .models import Obavestenje
from profil.models import Oblast
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Div, Layout, Submit
# from crispy_forms.templatetags import crispy_forms_filters


class ObavestenjeForm(forms.ModelForm):
    class Meta:
        model = Obavestenje
        fields = [
            'profil',
            'naslov',
            'tekst',
            'potpis',
        ]
        widgets = {
            'profil': forms.SelectMultiple(attrs={'id': 'myselect'})
        }
    

class OblastForm(forms.ModelForm):
    class Meta:
        model = Oblast
        fields = ['naziv']
