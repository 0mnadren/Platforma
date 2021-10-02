import os
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from recenzentPlatforma import settings
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

import random
import string

def my_hash():
    source = string.ascii_letters + string.digits
    return ''.join(random.choice(source) for i in range(64))


def validate_file_extension(self):
    """
    Proverava ekstenziju fajla da vidi da li je .pdf
    Ako nije dize ValidationError
    """
    extension = os.path.splitext(self.name)[1]  # [0] returns path+filename
    if extension.lower() in settings.CONTENT_TYPES:
        if self.size > int(settings.MAX_UPLOAD_SIZE):
            raise ValidationError(_(f'Veličina fajl-a mora da bude ispod'
                                    f' {filesizeformat(settings.MAX_UPLOAD_SIZE)}.'
                                    f' Trenutna veličina je {filesizeformat(self.size)}'))
    else:
        raise ValidationError('Nije podržan ovaj tip fajl-a. Mora biti .pdf formata!')


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Broj telefona treba da bude u sledećem formatu: '+999999999'."
                                     " Do 15 cifara je dozvoljeno.")
