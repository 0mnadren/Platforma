from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Stavio sam None kad se user registruje -->
    Da bi mogli da stavimo False kad ga odbiju i True kad ga prihvate
    """
    profile_accepted = models.BooleanField(default=None, null=True)


def accepted_check(user):
    return user.profile_accepted


