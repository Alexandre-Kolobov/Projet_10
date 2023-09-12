from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

def validate_age(value):
    if value < 15:
        raise ValidationError('Age must be at least 15.')

class User(AbstractUser):
    age = models.fields.IntegerField(blank=False, validators=[validate_age])
    can_be_contacted = models.fields.BooleanField()
    can_data_be_shared = models.fields.BooleanField()
    created_time = models.fields.DateTimeField(auto_now_add=True)
