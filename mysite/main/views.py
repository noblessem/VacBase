from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, Disease, Vaccination
from .forms import CreateNewList, Find,AddingForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# Create your views here.
from datetime import datetime

def index(response, id):

    ls = ToDoList.objects.get(id=id)
    if ls in response.user.todolist.all():
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Invalid Input")



        name = ls.name
        #item = ls.item_set.get(id=1)

        return render(response, 'main/list.html', {"ls": ls})
    else:
        return render(response, "main/view.html", {})


def home(response):
    if response.user.is_authenticated:
        form = Find()
        if len(response.user.groups.all()) > 0:
            users = []
            if response.user.groups.get(name='Doctors'):
                for user in User.objects.all():
                    if user.groups.filter(name='Doctors'):
                        print("He is doctor")
                    else:
                        users.append(user.username)
                return render(response, 'main/doctor_profile.html', {'users': users})
            elif response.method == "POST":
                if response.POST.get('find') == 'disease':
                    name = response.POST.get('name')
                    diseases = response.user.disease.filter(disease_name__contains=name)
                    vacs = response.user.vac.all().order_by('-vac_date')
                    return render(response, 'main/profile.html', {"diseases": diseases, "form": form, "vacs":vacs})
                elif response.POST.get('refresh') == 'refresh':
                    vacs = response.user.vac.all().order_by('-vac_date')
                    diseases = response.user.disease.all().order_by('-disease_date')
                    return render(response, 'main/profile.html', {"diseases": diseases, "form": form, "vacs": vacs})

                else:
                    name = response.POST.get('name')
                    vacs = response.user.vac.filter(vac_name__contains=name)
                    diseases = response.user.disease.all().order_by('-disease_date')

                    return render(response, 'main/profile.html', {"vacs": vacs, "form": form, "diseases": diseases})
        vacs = response.user.vac.all().order_by('-vac_date')
        diseases = response.user.disease.all().order_by('-disease_date')
        return render(response, 'main/profile.html', {"diseases": diseases, "form": form, "vacs": vacs})

    return render(response, 'main/home.html', {"name": "test"})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
            return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response, 'main/create.html', {"form": form})


def view(response):
    return render(response, "main/view.html", {})


def patient(response):
    if response.method == "POST":
        if response.POST.get('add') == 'disease':
            form = AddingForm()
            disease_name = response.POST.get('name')
            username = response.POST.get('username')
            patient = User.objects.get(username=username)
            disease = patient.disease.create(disease_name=disease_name, disease_date = datetime.now())
            patient_vacs = patient.vac.all()
            patient_diseases = patient.disease.all()
            disease.save()
            print(disease)
            return render(response, 'main/patient.html', {'vacs': patient_vacs, 'diseases': patient_diseases, 'patient': patient, 'form': form})

        if response.user.is_authenticated:
            if response.user.groups.get(name='Doctors'):
                print(response.POST)


                username = response.POST.get('username')
                patient = User.objects.get(username=username)
                patient_vacs = patient.vac.all()
                patient_diseases = patient.disease.all()
                print(patient)
                print(response.POST.get('username'))
                form = AddingForm()
                return render(response, 'main/patient.html', {'vacs': patient_vacs, 'diseases': patient_diseases, 'patient': patient, 'form': form})
    else:
        return HttpResponseRedirect('/')


