from django.urls import path
from Add_Patient import views

urlpatterns = [
    path('patient/', views.Add_Patient, name='patient'), 
]
