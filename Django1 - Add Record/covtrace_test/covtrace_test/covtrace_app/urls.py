from django.urls import path 
from . import views

#URLConf
urlpatterns = [
    path('hello/', views.say_hello, name="home"),
    path('join/', views.Add_Patient, name="join"),
]