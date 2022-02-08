from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    def __str__(self):
        return self.email


class Profile(models.Model):

    """ Trato este perfil como clientes, y estara disponibles las capacidadesd e clientes para los vendedores"""
    user  = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile", primary_key=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    address = models.CharField(max_length=170, null=True, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    personalized_password = models.CharField(max_length=15, default="fake_pass")
    #phone_number = PhoneNumberField(unique=True, blank=True) # no encuentro este modulo

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Vendor(models.Model):
    profile  = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="profile", primary_key=True)
    #is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.generalProfile}"
