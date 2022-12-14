from django.urls import path
from Covid_News import views

urlpatterns = [
    path('news/', views.News, name='news'),
]
