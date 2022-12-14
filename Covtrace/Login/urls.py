from django.urls import path
from Login import views

urlpatterns = [
    path('login/', views.Login_User, name="login"),  
    path('logout/', views.Logout_User, name="logout"),  
]