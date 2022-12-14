from django.shortcuts import render, redirect 
from Add_Patient.models import Positive_Detail, Patient_Detail, Recovered_Detail, Death_Detail, New_Death_Detail, \
    New_Positive_Detail, New_Recovered_Detail
from datetime import datetime, date, timedelta
import folium 
from folium import plugins

def Home(request):
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

    data = Patient_Detail.objects.all() 

    data_list = Patient_Detail.objects.values_list('latitude', 'longitude', 'population') 

    map1 = folium.Map(location=[14.116667, 122.949997],  tiles="CartoDB Dark_Matter",  zoom_start=11.50) 

    #plugins.HeatMap(data_list, gradient={0.0: 'red'}, min_opacity=0.4, blur = 18).add_to(map1)
    
    plugins.HeatMap(data_list, min_opacity=0.4, blur = 18).add_to(map1)
    plugins.Fullscreen().add_to(map1)
    map1 = map1._repr_html_()

    patients_dets_count = Positive_Detail.objects.all().count
    patients_recovered_count = Recovered_Detail.objects.all().count    
    patients_death_count = Death_Detail.objects.all().count

    new_patients_dets_count = New_Positive_Detail.objects.all().count
    new_patients_recovered_count = New_Recovered_Detail.objects.all().count    
    new_patients_death_count = New_Death_Detail.objects.all().count

    context = {
        'map1': map1,
        'patients_dets': patients_dets,
        'patients_recovered_count': patients_recovered_count,
        'patients_death_count': patients_death_count,
        'patients_dets_count': patients_dets_count,
        'new_patients_dets_count': new_patients_dets_count,
        'new_patients_recovered_count': new_patients_recovered_count,
        'new_patients_death_count': new_patients_death_count,
    }

    return render(request, "websites/index.html", context) 
