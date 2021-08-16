import os
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


# Proverava ekstenziju fajla da vidi da li je .pdf
# Ako nije dize ValidationError

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = '.pdf'
    if not ext.lower() == valid_extensions:
        raise ValidationError('Unsupported file extension.')


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. "
                                     "Up to 15 digits allowed.")

