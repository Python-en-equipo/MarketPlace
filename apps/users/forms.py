from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Seller, GeneralProfile

class UserForm(UserCreationForm):    

    class Meta:
        model = GeneralProfile
        fields = ["first_name", "last_name", "email", "password1", "password2"]
