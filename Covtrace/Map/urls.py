from django.urls import path
from Map import views

urlpatterns = [ 
    path('map/', views.New_Map, name='map'),
]
