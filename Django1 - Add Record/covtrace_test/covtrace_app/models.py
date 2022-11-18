from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Patient(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name} - {self.age}"

