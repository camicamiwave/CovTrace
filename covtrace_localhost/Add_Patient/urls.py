from django.urls import path
from Add_Patient import views

urlpatterns = [
    path('record/', views.AddPatient, name='record'),
]
