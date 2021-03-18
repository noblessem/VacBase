from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime


class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text


class Disease(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disease', null=True)
    disease_name = models.CharField(max_length=120)
    disease_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.disease_name


class Vaccination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vac', null=True)
    vac_name = models.CharField(max_length=120)
    vac_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.vac_name

