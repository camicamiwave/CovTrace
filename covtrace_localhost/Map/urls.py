from django.urls import path
from Map import views

urlpatterns = [
    path('daet_map/', views.Generate_Map, name='daet_map'),
]
