from django.urls import path
from Add_Patient import views

urlpatterns = [
    path('patient/', views.AddPatient, name='patient'), 
]
