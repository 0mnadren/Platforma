from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    error_messages = {
        'password_mismatch': _('Dva polja za lozinku se ne poklapaju.'),
    }

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
