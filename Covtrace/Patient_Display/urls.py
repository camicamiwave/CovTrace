from django.urls import path
from Patient_Display import views

urlpatterns = [
    path('display/', views.Display, name='display'),   
    path('get_recovered_patients/<primary_key>', views.Get_Recovered_Patients, name='get_recovered_patients'),
    path('get_deceased_patients/<primary_key>', views.Get_Deceased_Patients, name='get_deceased_patients'),
]
