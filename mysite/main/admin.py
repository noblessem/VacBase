from django.contrib import admin
from .models import ToDoList, Item,Disease, Vaccination
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(Disease)
admin.site.register(Vaccination)

