from django.shortcuts import render, redirect
from Add_Patient.models import Patient
from Home.models import Patient_List, New_Total_Number_Recovered_Patient, Total_Number_Recovered_Patient, Total_Number_Positive_Patient, New_Total_Number_Positive_Patient, New_Total_Number_Died_Patient, Total_Number_Died_Patient
from django.contrib.auth.models import User
from datetime import date

 
def Home(request): 
    patients = Patient.objects.all 
    patients_count = Patient.objects.all().count 

    date_today = date.today()
    
    All_Patients_List = Patient_List.objects.all

    Patients_Data = Patient.objects.all()
    
    
    for patient in Patients_Data: 
        if patient.status == "Positive":
            Save_Total_Positive_Patients(patient.id)
            Save_Patients_List(patient.id)
            if patient.recorded_date == date_today: 
                Save_New_Total_Positive_Patients(patient.id) 
            else:
                Delete_New_Total_Positive_Patients(patient.id)
        if patient.status == "Recovered":
            Save_Total_Recovered_Patients(patient.id) 
            Save_Patients_List(patient.id)
            if patient.recorded_date == date_today: 
                Save_New_Total_Recovered_Patients(patient.id) 
            else:
                Delete_New_Total_Recovered_Patients(patient.id) 
        if patient.status == "Died":
            Save_Total_Died_Patients(patient.id) 
            Save_Patients_List(patient.id)
            if patient.recorded_date == date_today: 
                Save_New_Total_Died_Patients(patient.id) 
            else:
                Delete_New_Total_Died_Patients(patient.id) 

    total_covid_cases = Total_Number_Positive_Patient.objects.all().count 
    total_recovered_cases = Total_Number_Recovered_Patient.objects.all().count 
    total_death_cases = Total_Number_Died_Patient.objects.all().count 
    new_total_covid_cases = New_Total_Number_Positive_Patient.objects.all().count 
    new_total_recovered_case = New_Total_Number_Recovered_Patient.objects.all().count 
    new_total_death_cases = New_Total_Number_Died_Patient.objects.all().count 

    context = { 
        'patients': patients,
        'patients_count': patients_count,
        'All_Patients_List': All_Patients_List,
        'total_covid_cases': total_covid_cases,
        'total_recovered_cases': total_recovered_cases,
        'total_death_cases': total_death_cases,
        'new_total_covid_cases': new_total_covid_cases,
        'new_total_recovered_case': new_total_recovered_case,
        'new_total_death_cases': new_total_death_cases,
    }

    return render(request, "websites/home.html", context)


#-------------------------------------PATIENT LIST-------------------------------------

def Save_Patients_List(patient_id):
    new_total_positive_patients = Patient.objects.get(pk=patient_id) 

    number_new_pos_patient = Patient_List()
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

#-------------------------------------POSITIVE-------------------------------------

def Save_Total_Positive_Patients(patient_id):
    new_total_positive_patients = Patient.objects.get(pk=patient_id) 

    number_new_pos_patient = Total_Number_Positive_Patient()
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
    new_total_recovered_patients = Patient.objects.get(pk=patient_id)   
    
    new_total_recovered_patients.delete()

    return redirect('home')

#-------------------------------------POSITIVE-------------------------------------

#-------------------------------------RECOVERED-------------------------------------

def Save_Total_Recovered_Patients(patient_id):
    new_total_positive_patients = Patient.objects.get(pk=patient_id) 

    number_new_pos_patient = Total_Number_Recovered_Patient()
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

#-------------------------------------RECOVERED-------------------------------------


#-------------------------------------DIED-------------------------------------

def Save_Total_Died_Patients(patient_id):
    new_total_positive_patients = Patient.objects.get(pk=patient_id) 

    number_new_pos_patient = Total_Number_Died_Patient()
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
    new_total_recovered_patients = Patient.objects.get(pk=patient_id)   

    new_total_recovered_patients.delete()

    return redirect('home')

#-------------------------------------RECOVERED-------------------------------------

#work in progress ----------------------------------------
def Get_Recovered_Patient(patient_id):
    Patients_List = Patient_List.objects.get(pk=patient_id) 

    print("helloooo")
    #Patients_List.delete()

    return redirect('home')
#---------------------------------------------------------