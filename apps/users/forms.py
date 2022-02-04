from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Employee, GeneralProfile

class UserForm(UserCreationForm):    

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class GeneralFormUser(forms.ModelForm):
    class Meta:
        model = GeneralProfile
        fields = ["first_name", "last_name",  "email",]
        labels = {
                "first_name": "Nombre",
                "last_name": "Apellido",
                "email": "Correo electrónico",
              
                }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["phone_number", "address"]
        labels = {
                "phone_number": "Número de celular",
                "address": "Dirección",
                }