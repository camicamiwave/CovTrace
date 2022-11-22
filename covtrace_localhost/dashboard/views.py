from django.shortcuts import render
import folium
from .models import Data
from folium import plugins
#templates for map ex. tiles="CartoDB Dark_Matter",
# Create your views here.
#daet coordinates 14.116667, 122.949997

def index(request):
    data = Data.objects.all()
    data_list = Data.objects.values_list('latitude', 'longitude', 'population')
    
    map1 = folium.Map(location=[14.116667, 122.949997], tiles="CartoDB Dark_Matter",  zoom_start=2)
    
    plugins.HeatMap(data_list).add_to(map1)
    plugins.Fullscreen().add_to(map1)
    map1 = map1._repr_html_()
    context = {
        'map1': map1
    }
    return render(request, 'dashboard/index.html', context)

