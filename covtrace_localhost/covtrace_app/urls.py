from django.urls import path
from . import views

urlpatterns = [ 
    path("home/", views.home, name="home"),
    path('record/', views.Add_Patient, name="record"),
    path('content/', views.Map, name="content"),
]
