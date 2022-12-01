from django.shortcuts import render, redirect
from Add_Patient.models import Patient
from Home.models import Total_Positive_Patient, Total_Recovered_Patient, Total_Died_Patient, New_Total_Number_Positive_Patient, New_Total_Number_Recovered_Patient, New_Total_Number_Died_Patient
from django.contrib.auth.models import User
from datetime import datetime, date 
import datetime

def New_Home(request):
     
    patients = Patient.objects.all  

    date_today = date.today()
    
    Patient_List = Patient.objects.all()
    for patient in Patient_List:
        if patient.status == "Positive":
            if patient.recorded_date == date_today:
                Save_New_Total_Positive_Patients(patient.id) 
            else:
                Delete_New_Total_Positive_Patients(patient.id)
        if patient.status == "Recovered":
            if patient.recorded_date == date_today: 
                Save_New_Total_Recovered_Patients(patient.id)
            else:
                Delete_New_Total_Recovered_Patients(patient.id)  
        if patient.status == "Died":
            if patient.recorded_date == date_today:
                Save_New_Total_Died_Patients(patient.id)  
            else:    
                Delete_New_Total_Died_Patients(patient.id)

    new_total_positive_patients_count = New_Total_Number_Positive_Patient.objects.all().count
    new_total_recovered_patients_count = New_Total_Number_Recovered_Patient.objects.all().count
    new_death_patients_count = New_Total_Number_Died_Patient.objects.all().count
    total_positive_patients_count = Total_Positive_Patient.objects.all().count 
    total_recovered_patients_count = Total_Recovered_Patient.objects.all().count 
    total_death_patients_count = Total_Died_Patient.objects.all().count   


    context = { 
        'date_today': date_today,
        'patients': patients,
        'new_total_positive_patients_count': new_total_positive_patients_count,
        'new_total_recovered_patients_count': new_total_recovered_patients_count,
        'new_death_patients_count': new_death_patients_count,
        'total_positive_patients_count': total_positive_patients_count,
        'total_recovered_patients_count': total_recovered_patients_count,
        'total_death_patients_count': total_death_patients_count,
    }  
    
    return render(request, "websites/index.html", {})

def Home(request): 
    patients = Patient.objects.all  

    date_today = date.today()
    
    Patient_List = Patient.objects.all()
    for patient in Patient_List:
        if patient.status == "Positive":
            if patient.recorded_date == date_today:
                Save_New_Total_Positive_Patients(patient.id) 
            else:
                Delete_New_Total_Positive_Patients(patient.id)
        if patient.status == "Recovered":
            if patient.recorded_date == date_today: 
                Save_New_Total_Recovered_Patients(patient.id)
            else:
                Delete_New_Total_Recovered_Patients(patient.id)  
        if patient.status == "Died":
            if patient.recorded_date == date_today:
                Save_New_Total_Died_Patients(patient.id)  
            else:    
                Delete_New_Total_Died_Patients(patient.id)

    new_total_positive_patients_count = New_Total_Number_Positive_Patient.objects.all().count
    new_total_recovered_patients_count = New_Total_Number_Recovered_Patient.objects.all().count
    new_death_patients_count = New_Total_Number_Died_Patient.objects.all().count
    total_positive_patients_count = Total_Positive_Patient.objects.all().count 
    total_recovered_patients_count = Total_Recovered_Patient.objects.all().count 
    total_death_patients_count = Total_Died_Patient.objects.all().count   


    context = { 
        'date_today': date_today,
        'patients': patients,
        'new_total_positive_patients_count': new_total_positive_patients_count,
        'new_total_recovered_patients_count': new_total_recovered_patients_count,
        'new_death_patients_count': new_death_patients_count,
        'total_positive_patients_count': total_positive_patients_count,
        'total_recovered_patients_count': total_recovered_patients_count,
        'total_death_patients_count': total_death_patients_count,
    }  
 
    return render(request, "websites/home.html", context)



#-------------------------------------DIED PATIENTS-------------------------------------

def Save_New_Total_Died_Patients(patient_id):
    new_total_positive_patients = Patient.objects.get(pk=patient_id) 

    number_new_pos_patient = New_Total_Number_Died_Patient()
    number_new_pos_patient.id = new_total_positive_patients.id
    number_new_pos_patient.name = new_total_positive_patients.name
    number_new_pos_patient.birthday = new_total_positive_patients.birthday
    number_new_pos_patient.age = new_total_positive_patients.age
    number_new_pos_patient.gender = new_total_positive_patients.gender
    number_new_pos_patient.barangay = new_total_positive_patients.barangay
    number_new_pos_patient.status = new_total_positive_patients.status
    number_new_pos_patient.date_admitted = new_total_positive_patients.date_admitted
    number_new_pos_patient.population = new_total_positive_patients.population
    number_new_pos_patient.latitude = new_total_positive_patients.latitude
    number_new_pos_patient.longitude = new_total_positive_patients.longitude

    number_new_pos_patient.save()

    return redirect('home')

def Delete_New_Total_Died_Patients(patient_id):
    new_total_positive_patients = Patient.objects.get(pk=patient_id)  

    print("EYYY", new_total_positive_patients.name, new_total_positive_patients.recorded_date)

    new_total_positive_patients.delete()

    return redirect('home')


#-------------------------------------DIED PATIENTS-------------------------------------



#-------------------------------------RECOVERED PATIENTS-------------------------------------

def Save_New_Total_Recovered_Patients(patient_id):
    new_total_positive_patients = Patient.objects.get(pk=patient_id) 

    number_new_pos_patient = New_Total_Number_Recovered_Patient()
    number_new_pos_patient.id = new_total_positive_patients.id
    number_new_pos_patient.name = new_total_positive_patients.name
    number_new_pos_patient.birthday = new_total_positive_patients.birthday
    number_new_pos_patient.age = new_total_positive_patients.age
    number_new_pos_patient.gender = new_total_positive_patients.gender
    number_new_pos_patient.barangay = new_total_positive_patients.barangay
    number_new_pos_patient.status = new_total_positive_patients.status
    number_new_pos_patient.date_admitted = new_total_positive_patients.date_admitted
    number_new_pos_patient.population = new_total_positive_patients.population
    number_new_pos_patient.latitude = new_total_positive_patients.latitude
    number_new_pos_patient.longitude = new_total_positive_patients.longitude

    number_new_pos_patient.save()

    return redirect('home')

def Delete_New_Total_Recovered_Patients(patient_id):
    new_total_recovered_patients = Patient.objects.get(pk=patient_id)   

    new_total_recovered_patients.delete()

    return redirect('home')


#-------------------------------------RECOVERED PATIENTS-------------------------------------


#-------------------------------------POSITIVE PATIENTS-------------------------------------

def Save_New_Total_Positive_Patients(patient_id):
    new_total_positive_patients = Patient.objects.get(pk=patient_id) 

    number_new_pos_patient = New_Total_Number_Positive_Patient()
    number_new_pos_patient.id = new_total_positive_patients.id
    number_new_pos_patient.name = new_total_positive_patients.name
    number_new_pos_patient.birthday = new_total_positive_patients.birthday
    number_new_pos_patient.age = new_total_positive_patients.age
    number_new_pos_patient.gender = new_total_positive_patients.gender
    number_new_pos_patient.barangay = new_total_positive_patients.barangay
    number_new_pos_patient.status = new_total_positive_patients.status
    number_new_pos_patient.date_admitted = new_total_positive_patients.date_admitted
    number_new_pos_patient.population = new_total_positive_patients.population
    number_new_pos_patient.latitude = new_total_positive_patients.latitude
    number_new_pos_patient.longitude = new_total_positive_patients.longitude

    number_new_pos_patient.save()

    return redirect('home')

def Delete_New_Total_Positive_Patients(patient_id):
    new_total_positive_patients = Patient.objects.get(pk=patient_id)  

    print("EYYY", new_total_positive_patients.name, new_total_positive_patients.recorded_date)

    new_total_positive_patients.delete()

    return redirect('home')


#-------------------------------------POSITIVE PATIENTS-------------------------------------


#------------------------------WORK IN PROGRESS-----------------------------------------

def Get_Recovered_Patient(patient_id):
    new_total_positive_patients = Patient.objects.get(pk=patient_id) 

    new_total_positive_patients.delete()

    return redirect('home')

def Get_Died_Patient(patient_id):
    new_total_positive_patients = Patient.objects.get(pk=patient_id) 

    new_total_positive_patients.delete()

    return redirect('home')


#------------------------------WORK IN PROGRESS-----------------------------------------