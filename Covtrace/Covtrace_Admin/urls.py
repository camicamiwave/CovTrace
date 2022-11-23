from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Home.urls")),
    path('', include("Add_Patient.urls")),
    path('', include("Map.urls")),
    path('', include("About_Us.urls")),
    path('', include("Login.urls")), 
    path('', include("Covid_News.urls")), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('officials/', include("Login.urls")),
    
]
