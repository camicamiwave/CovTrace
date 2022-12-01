from django.urls import path
from Home import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('new_home/', views.New_Home, name='new_home'),
    path('get_recovered_patient/<patient_id>', views.Get_Recovered_Patient, name='get_recovered_patient'),
    path('get_died_patient/<patient_id>', views.Get_Died_Patient, name='get_died_patient'), 
]
