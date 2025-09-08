from django import forms
from .models import Participant


class RegistrationForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=100)
    phone = forms.CharField(label="Телефон", max_length=20)
    email = forms.EmailField(label="Email")
