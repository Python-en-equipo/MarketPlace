from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    
    def __str__(self):
        return self.email