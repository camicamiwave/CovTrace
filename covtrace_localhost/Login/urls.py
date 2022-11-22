from django.urls import path
from . import views

urlpatterns = [ 
    path("login/", views.User_login, name="login"),
]

