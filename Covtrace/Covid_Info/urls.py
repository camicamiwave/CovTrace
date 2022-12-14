from django.urls import path
from Covid_Info import views

urlpatterns = [
    path('covid_info/', views.Covid_Info_Page, name='covid_info'),
]
