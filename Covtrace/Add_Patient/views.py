from django.shortcuts import render
from Add_Patient.forms import PatientForm
from Add_Patient.forms import New_Positive_Cases_Patient, Total_Positive_Cases_Patient

def Add_Patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST or None)
        new_pos_form = New_Positive_Cases_Patient(request.POST or None)
        total_pos_form = Total_Positive_Cases_Patient(request.POST or None)
        if form.is_valid():
            form.save()
            new_pos_form.save()
            total_pos_form.save()
        return render(request, "record/add_patient.html", {}) 
    else:
        return render(request, "record/add_patient.html", {})