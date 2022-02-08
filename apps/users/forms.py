from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Vendor, Profile

class UserForm(UserCreationForm):    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CustomProfileForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "address"]
        # labels = {
        #         "first_name": "Nombre",
        #         "last_name": "Apellido",
        #         "email": "Correo electrónico",
        #         }



class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ("__all__")
        # labels = { 
        #         }