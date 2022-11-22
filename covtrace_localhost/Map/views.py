from django.shortcuts import render
from Add_Patient.models import Patient   
import folium 
from folium import plugins

def Generate_Map(request):
    data = Patient.objects.all()
    data_list = Patient.objects.values_list('latitude', 'longitude', 'population')
    
    map1 = folium.Map(location=[14.116667, 122.949997], tiles="CartoDB Dark_Matter",  zoom_start=10)
    
    plugins.HeatMap(data_list).add_to(map1)
    plugins.Fullscreen().add_to(map1)
    map1 = map1._repr_html_()
    context = {
        'map1': map1
    }
    return render(request, 'daet_map/map.html', context)
 