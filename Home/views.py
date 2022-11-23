from django.shortcuts import render
from Add_Patient.models import Patient
from django.contrib.auth.models import User

 
def Home(request): 
    patients = Patient.objects.all 
    patients_count = Patient.objects.all().count 
    context = { 
        'patients': patients,
        'patients_count': patients_count
    }

    return render(request, "websites/home.html", context)