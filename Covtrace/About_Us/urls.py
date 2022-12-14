from django.urls import path
from About_Us import views

urlpatterns = [
    path('aboutus/', views.About_Us_Page, name='aboutus'),
]
