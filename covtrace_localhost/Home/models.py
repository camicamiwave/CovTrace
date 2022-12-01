from django.db import models
import geocoder 
from django.contrib.auth.models import User  
from django.utils import timezone
# Create your models here.


class New_Total_Number_Died_Patient(models.Model):
    recorded_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_admitted = models.DateField("Date Admitted (mm/dd/yyyy):", auto_now_add=False, auto_now=False, blank=True)

    population = models.FloatField(default=1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.barangay).lat
        self.longitude = geocoder.osm(self.barangay).lng

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Patient No. {self.id}. {self.name} - {self.barangay} - {self.recorded_date}" 

class New_Total_Number_Recovered_Patient(models.Model):
    recorded_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_admitted = models.DateField("Date Admitted (mm/dd/yyyy):", auto_now_add=False, auto_now=False, blank=True)

    population = models.FloatField(default=1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.barangay).lat
        self.longitude = geocoder.osm(self.barangay).lng

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Patient No. {self.id}. {self.name} - {self.barangay} - {self.recorded_date}" 

class New_Total_Number_Positive_Patient(models.Model):
    recorded_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_admitted = models.DateField("Date Admitted (mm/dd/yyyy):", auto_now_add=False, auto_now=False, blank=True)

    population = models.FloatField(default=1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.barangay).lat
        self.longitude = geocoder.osm(self.barangay).lng

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Patient No. {self.id}. {self.name} - {self.barangay} - {self.recorded_date}" 

class Total_Recovered_Patient(models.Model):
    recorded_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_admitted = models.DateField("Date Admitted (mm/dd/yyyy):", auto_now_add=False, auto_now=False, blank=True)

    population = models.FloatField(default=1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.barangay).lat
        self.longitude = geocoder.osm(self.barangay).lng

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Patient No. {self.id}. {self.name} - {self.barangay} - {self.recorded_date}" 


class Total_Positive_Patient(models.Model):
    recorded_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_admitted = models.DateField("Date Admitted (mm/dd/yyyy):", auto_now_add=False, auto_now=False, blank=True)

    population = models.FloatField(default=1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.barangay).lat
        self.longitude = geocoder.osm(self.barangay).lng

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Patient No. {self.id}. {self.name} - {self.barangay} - {self.recorded_date}" 

class Total_Died_Patient(models.Model):
    recorded_date = models.DateField(default=timezone.now)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birthday = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_admitted = models.DateField("Date Admitted (mm/dd/yyyy):", auto_now_add=False, auto_now=False, blank=True)

    population = models.FloatField(default=1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.barangay).lat
        self.longitude = geocoder.osm(self.barangay).lng

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Patient No. {self.id}. {self.name} - {self.barangay} - {self.recorded_date}" 

