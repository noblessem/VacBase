from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .forms import RegisterForm
# Create your views here.


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        print(response.POST)
        if form.is_valid():
            if response.POST.get('is_doctor') == 'on':
                my_group = Group.objects.get(name='Doctors')
                response.user.groups.add(my_group)
            form.save()
            return redirect("/")

    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})
