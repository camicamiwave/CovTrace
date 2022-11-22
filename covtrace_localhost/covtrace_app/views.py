from django.shortcuts import render
from .forms import PatientForm
from .models import Patient 
import folium 
from folium import plugins


#calling the url
def home(request):
    #calling all data in database
    
    all_patients = Patient.objects.all

    return render(request,"dashboard/home.html", {'all': all_patients})

def Add_Patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'dashboard/add_record.html', {}) 
    else:
        return render(request, 'dashboard/add_record.html', {})  

def Content(request):
    return render(request, "dashboard/hello.html", {})

def Map(request):
    data = Patient.objects.all()
    data_list = Patient.objects.values_list('latitude', 'longitude', 'population')
    
    map1 = folium.Map(location=[14.116667, 122.949997], tiles="CartoDB Dark_Matter",  zoom_start=10)
    
    plugins.HeatMap(data_list).add_to(map1)
    plugins.Fullscreen().add_to(map1)
    map1 = map1._repr_html_()
    context = {
        'map1': map1
    }
    return render(request, 'dashboard/map.html', context)
