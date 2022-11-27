from django.urls import path
from Home import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('get_recovered_patient/<patient_id>', views.Get_Recovered_Patient, name='get_recovered_patient'),
]
