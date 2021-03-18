from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=60, required=True)
    last_name = forms.CharField(max_length=120, required=True)
    is_doctor = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2", "is_doctor"]


