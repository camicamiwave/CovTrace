from django.shortcuts import render
from Add_Patient.models import Patient_Detail    
from Add_Patient.models import Positive_Detail, Patient_Detail, Recovered_Detail, Death_Detail, New_Death_Detail, \
    New_Positive_Detail, New_Recovered_Detail
import folium 
from folium import plugins
 
def New_Map(request):
    data = Patient_Detail.objects.all() 

    data_list = Patient_Detail.objects.values_list('latitude', 'longitude', 'population') 

    map1 = folium.Map(location=[14.116667, 122.949997],  tiles="CartoDB Dark_Matter",  zoom_start=11.50) 

    #plugins.HeatMap(data_list, gradient={0.0: 'red'}, min_opacity=0.4, blur = 18).add_to(map1)
    
    plugins.HeatMap(data_list, min_opacity=0.4, blur = 18).add_to(map1)
    plugins.Fullscreen().add_to(map1)
    map1 = map1._repr_html_()
    
    patients_dets = Patient_Detail.objects.all

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

    return render(request, 'daet_map.html', context)