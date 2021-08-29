import os
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from recenzentPlatforma import settings
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _


def validate_file_extension(self):
    """
    Proverava ekstenziju fajla da vidi da li je .pdf
    Ako nije dize ValidationError
    """
    extension = os.path.splitext(self.name)[1]  # [0] returns path+filename
    if extension.lower() in settings.CONTENT_TYPES:
        if self.size > int(settings.MAX_UPLOAD_SIZE):
            raise ValidationError(_(f'Please keep filesize under {filesizeformat(settings.MAX_UPLOAD_SIZE)}. Current filesize {filesizeformat(self.size)}'))
    else:
        raise ValidationError('Unsupported file extension.')


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: '+999999999'. "
                                     "Up to 15 digits allowed.")
