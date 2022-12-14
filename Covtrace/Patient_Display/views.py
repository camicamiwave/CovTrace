from django.shortcuts import render, redirect 
from Add_Patient.models import Positive_Detail, Patient_Detail, Recovered_Detail, Death_Detail, New_Death_Detail, \
    New_Positive_Detail, New_Recovered_Detail
from datetime import datetime, date, timedelta

def Display(request):
    patients_dets = Patient_Detail.objects.all

    date_today = date.today() 
    one_date_ahead = date.today() + timedelta(days=1)
    
    Details_Postive_Patients = New_Positive_Detail.objects.all

    positive_patients = New_Positive_Detail.objects.all()
    recovered_patients = New_Recovered_Detail.objects.all()
    death_patients = New_Death_Detail.objects.all()

    for patient in positive_patients: 
        if patient.date_admitted != date_today:
            print(patient.date_admitted)
            Details_Postive_Patients = New_Positive_Detail.objects.get(pk=patient.id) 
            Details_Postive_Patients.delete() 
    
    for patient in recovered_patients: 
        if patient.recovered_date != date_today:
            print(patient.date_admitted) 
            Details_Recovered_Patients = New_Recovered_Detail.objects.get(pk=patient.id) 
            Details_Recovered_Patients.delete() 

    for patient in death_patients:
        if patient.death_date != date_today:
            print(patient.date_admitted)  
            Details_Deaths_Patients = New_Death_Detail.objects.get(pk=patient.id) 
            Details_Deaths_Patients.delete()      
        
    patients_dets_count = Positive_Detail.objects.all().count
    patients_recovered_count = Recovered_Detail.objects.all().count    
    patients_death_count = Death_Detail.objects.all().count

    new_patients_dets_count = New_Positive_Detail.objects.all().count
    new_patients_recovered_count = New_Recovered_Detail.objects.all().count    
    new_patients_death_count = New_Death_Detail.objects.all().count

    context = {
        'patients_dets': patients_dets,
        'patients_recovered_count': patients_recovered_count,
        'patients_death_count': patients_death_count,
        'patients_dets_count': patients_dets_count,
        'new_patients_dets_count': new_patients_dets_count,
        'new_patients_recovered_count': new_patients_recovered_count,
        'new_patients_death_count': new_patients_death_count,
    }

    return render(request, "urls/display.html", context)  
  
def Get_Recovered_Patients(request, primary_key):
    patients_dets = Patient_Detail.objects.all
    patients = Patient_Detail.objects.get(pk=primary_key)

    one_date_ahead = date.today() + timedelta(days=1) 

    #ATTRIBUTES
    total_recovered_patients = Recovered_Detail()
    total_recovered_patients.id = patients.id
    total_recovered_patients.name = patients.name
    total_recovered_patients.age = patients.age
    total_recovered_patients.gender = patients.gender
    total_recovered_patients.barangay = patients.barangay
    total_recovered_patients.status = patients.status
    total_recovered_patients.date_admitted = patients.date_admitted
    total_recovered_patients.recovered_date = date.today()
    total_recovered_patients.population = patients.population
    total_recovered_patients.latitude = patients.latitude
    total_recovered_patients.longitude = patients.longitude 

    total_recovered_patients.save()

    #NEW RECOVERED PATIENTS
    new_total_recovered_patients = New_Recovered_Detail()
    new_total_recovered_patients.id = patients.id
    new_total_recovered_patients.name = patients.name
    new_total_recovered_patients.age = patients.age
    new_total_recovered_patients.gender = patients.gender
    new_total_recovered_patients.barangay = patients.barangay
    new_total_recovered_patients.status = patients.status
    new_total_recovered_patients.date_admitted = patients.date_admitted
    new_total_recovered_patients.recovered_date = date.today()
    new_total_recovered_patients.population = patients.population
    new_total_recovered_patients.latitude = patients.latitude
    new_total_recovered_patients.longitude = patients.longitude

    new_total_recovered_patients.save()

    print(patients)
    patients.delete()
    
    patients_dets_count = Positive_Detail.objects.all().count
    patients_recovered_count = Recovered_Detail.objects.all().count    
    patients_death_count = Death_Detail.objects.all().count

    new_patients_dets_count = New_Positive_Detail.objects.all().count
    new_patients_recovered_count = New_Recovered_Detail.objects.all().count    
    new_patients_death_count = New_Death_Detail.objects.all().count

    context = {
        'patients_dets': patients_dets,
        'patients_recovered_count': patients_recovered_count,
        'patients_death_count': patients_death_count,
        'patients_dets_count': patients_dets_count,
        'new_patients_dets_count': new_patients_dets_count,
        'new_patients_recovered_count': new_patients_recovered_count,
        'new_patients_death_count': new_patients_death_count,
    }

    return render(request, "urls/display.html", context)

def Get_Deceased_Patients(request, primary_key):
    patients_dets = Patient_Detail.objects.all
    patients = Patient_Detail.objects.get(pk=primary_key)

    one_date_ahead = date.today() + timedelta(days=1) 

    #ATTRIBUTES
    total_death_patients = Death_Detail()
    total_death_patients.id = patients.id
    total_death_patients.name = patients.name
    total_death_patients.age = patients.age
    total_death_patients.gender = patients.gender
    total_death_patients.barangay = patients.barangay
    total_death_patients.status = patients.status
    total_death_patients.date_admitted = patients.date_admitted
    total_death_patients.recovered_date = date.today()
    total_death_patients.population = patients.population
    total_death_patients.latitude = patients.latitude
    total_death_patients.longitude = patients.longitude

    total_death_patients.save()

    #NEW DEATH PATIENTS
    new_total_death_patients = New_Death_Detail()
    new_total_death_patients.id = patients.id
    new_total_death_patients.name = patients.name
    new_total_death_patients.age = patients.age
    new_total_death_patients.gender = patients.gender
    new_total_death_patients.barangay = patients.barangay
    new_total_death_patients.status = patients.status
    new_total_death_patients.date_admitted = patients.date_admitted
    new_total_death_patients.death_date = date.today()
    new_total_death_patients.population = patients.population
    new_total_death_patients.latitude = patients.latitude
    new_total_death_patients.longitude = patients.longitude

    new_total_death_patients.save()

    print(patients)
    patients.delete()
    
    patients_dets_count = Positive_Detail.objects.all().count
    patients_recovered_count = Recovered_Detail.objects.all().count    
    patients_death_count = Death_Detail.objects.all().count

    new_patients_dets_count = New_Positive_Detail.objects.all().count
    new_patients_recovered_count = New_Recovered_Detail.objects.all().count    
    new_patients_death_count = New_Death_Detail.objects.all().count

    context = {
        'patients_dets': patients_dets,
        'patients_recovered_count': patients_recovered_count,
        'patients_death_count': patients_death_count,
        'patients_dets_count': patients_dets_count,
        'new_patients_dets_count': new_patients_dets_count,
        'new_patients_recovered_count': new_patients_recovered_count,
        'new_patients_death_count': new_patients_death_count,
    }


    return render(request, "urls/display.html", context)

    #return redirect("home", context) 