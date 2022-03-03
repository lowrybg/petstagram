from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30


    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator
        )

    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,

    )