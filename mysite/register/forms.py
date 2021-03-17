from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField(max_length=60)
    surname = forms.CharField(max_length=120)
    class Meta:
        model = User
        fields = ["firstname", "surname", "username", "email", "password1", "password2"]


