from django.shortcuts import render
from .forms import PatientForm

def AddPatient(request):
    if request.method == "POST":
        form = PatientForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, "record/add_record.html", {}) 
    else:
        return render(request, "record/add_record.html", {})  