from django.db import models 
from django.contrib.auth.models import User
import geocoder 
from django.utils import timezone
from django.db import models 

barangay = {
        'Alawihao': [14.1080, 122.9246],
        'Awitan': [14,1375, 122.9620],
        'Bagasbas': [14,1369, 122.9620],
        'Barangay I': [14.1115, 122.9590],
        'Barangay II': [14.1068, 122.9562],
        'Barangay III': [14.1116, 122.9546],
        'Barangay IV': [14.1170, 122.9496],
        'Barangay V': [14.1201, 122.9512],
        'Barangay VI': [14.1194, 122.9571],
        'Barangay VII': [14.1171, 122.9601],
        'Barangay VIII': [14.1137, 122.9587],
        'Bibirao': [14.0955, 122.9247],
        'Borabod': [14.1279, 122.9645], 
        'Calasgasan': [14.0856, 122.9362],
        'Camambugan': [14.1079, 122.9485],
        'Cobangbang': [14.1057, 122.9610],
        'Dogongan': [14.1000, 122.9032],
        'Gahonon': [14.1277, 122.9514],
        'Gubat': [14.1144, 122.9717], 
        'Lag-on': [14.1149, 122.9380],
        'Magang': [14.1007, 122.9549],
        'Mambalite': [14.0945, 122.9823],
        'Mancruz': [14.0918, 122.9548],
        'Pamorangon': [14.0939, 122.9632],
        'San Isidro': [14.1050, 122.9820]
    }


class Patient_Detail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_admitted = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    
    population = models.FloatField(default=1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    def save(self, *args, **kwargs):
        #self.latitude = geocoder.osm(self.barangay).lat
        #self.longitude = geocoder.osm(self.barangay).lng

        if self.barangay == 'Alawihao':
            self.latitude = 14.1080
            self.longitude =  122.9246

            return super().save(*args, **kwargs)
     
        if self.barangay == 'Awitan':
            self.latitude = 14.1375
            self.longitude =  122.9620

            return super().save(*args, **kwargs)
        
        if self.barangay == 'Bagasbas':
            self.latitude = 14.1369
            self.longitude =  122.9620  

            return super().save(*args, **kwargs)
            
        if self.barangay == 'Barangay I':
            self.latitude = 14.1115
            self.longitude =  122.9590 

            return super().save(*args, **kwargs)
        
        if self.barangay == 'Barangay II':
            self.latitude = 14.1068
            self.longitude =  122.9562

            return super().save(*args, **kwargs)

        if self.barangay == 'Barangay III':
            self.latitude = 14.1116
            self.longitude = 122.9546

            return super().save(*args, **kwargs)
        
        if self.barangay == 'Barangay IV':
            self.latitude = 14.1170
            self.longitude =  122.9496

            return super().save(*args, **kwargs)
        
        if self.barangay == 'Barangay V':
            self.latitude = 14.1201
            self.longitude =  122.9512

            return super().save(*args, **kwargs)

        if self.barangay == 'Barangay VI':
            self.latitude = 14.1194
            self.longitude = 122.9571

            return super().save(*args, **kwargs)
        
        if self.barangay == 'Barangay VII':
            self.latitude = 14.1171
            self.longitude =  122.9601

            return super().save(*args, **kwargs)
        
        if self.barangay == 'Barangay VIII':
            self.latitude = 14.1137
            self.longitude =  122.9587

            return super().save(*args, **kwargs)
            
        if self.barangay == 'Bibirao':
            self.latitude = 14.0955
            self.longitude =  122.9247

            return super().save(*args, **kwargs)
             
        if self.barangay == 'Borabod':
            self.latitude = 14.1279
            self.longitude =  122.9645

            return super().save(*args, **kwargs)
             
        if self.barangay == 'Calasgasan':
            self.latitude = 14.0856
            self.longitude =  122.9362

            return super().save(*args, **kwargs)

        if self.barangay == 'Camambugan':
            self.latitude = 14.1079
            self.longitude =  122.9485

            return super().save(*args, **kwargs)
        
        if self.barangay == 'Cobangbang':
            self.latitude = 14.1057
            self.longitude =  122.9610

            return super().save(*args, **kwargs)
        
        if self.barangay == 'Dogongan':
            self.latitude = 14.1000
            self.longitude =  122.9032

            return super().save(*args, **kwargs)

        if self.barangay == 'Gahonon':
            self.latitude = 14.1277
            self.longitude =  122.9514

            return super().save(*args, **kwargs)
        
        if self.barangay == 'Gubat':
            self.latitude = 14.1144
            self.longitude =  122.9717

            return super().save(*args, **kwargs)
        
        if self.barangay == 'Lag-on':
            self.latitude = 14.1149
            self.longitude =  122.9380

            return super().save(*args, **kwargs)
        
        if self.barangay == 'Magang':
            self.latitude = 14.1007
            self.longitude =  122.9549

            return super().save(*args, **kwargs)
        
        if self.barangay == 'Mambalite':
            self.latitude = 14.0945
            self.longitude =  122.9823

            return super().save(*args, **kwargs)
        
        if self.barangay == 'Mancruz':
            self.latitude = 14.0918
            self.longitude =  122.9548

            return super().save(*args, **kwargs)
  
        if self.barangay == 'Pamorangon':
            self.latitude = 14.0939
            self.longitude =  122.9632

            return super().save(*args, **kwargs)
        
        if self.barangay == 'San Isidro':
            self.latitude = 14.1050
            self.longitude =  122.9820

            return super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Patient No. {self.id}. {self.name} - {self.barangay}" 

class Recovered_Detail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_admitted = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    recovered_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    population = models.FloatField(default=1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    '''def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.barangay).lat
        self.longitude = geocoder.osm(self.barangay).lng

        return super().save(*args, **kwargs)'''

    def __str__(self):
        return f"Patient No. {self.id}. {self.name} - {self.barangay}" 

class Death_Detail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_admitted = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    recovered_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    population = models.FloatField(default=1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    '''def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.barangay).lat
        self.longitude = geocoder.osm(self.barangay).lng

        return super().save(*args, **kwargs)'''

    def __str__(self):
        return f"Patient No. {self.id}. {self.name} - {self.barangay}" 

class Positive_Detail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_admitted = models.DateField(auto_now_add=False, auto_now=False, blank=True) 

    population = models.FloatField(default=1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    '''def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.barangay).lat
        self.longitude = geocoder.osm(self.barangay).lng

        return super().save(*args, **kwargs)'''

    def __str__(self):
        return f"Patient No. {self.id}. {self.name} - {self.barangay}" 

class New_Recovered_Detail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_admitted = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    recovered_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    population = models.FloatField(default=1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    '''def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.barangay).lat
        self.longitude = geocoder.osm(self.barangay).lng

        return super().save(*args, **kwargs)'''

    def __str__(self):
        return f"Patient No. {self.id}. {self.name} - {self.barangay}" 

class New_Death_Detail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_admitted = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    death_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    population = models.FloatField(default=1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    '''def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.barangay).lat
        self.longitude = geocoder.osm(self.barangay).lng

        return super().save(*args, **kwargs)'''

    def __str__(self):
        return f"Patient No. {self.id}. {self.name} - {self.barangay}" 


class New_Positive_Detail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    barangay = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    date_admitted = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    population = models.FloatField(default=1)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    '''def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.barangay).lat
        self.longitude = geocoder.osm(self.barangay).lng

        return super().save(*args, **kwargs)'''
    def __str__(self):
        return f"Patient No. {self.id}. {self.name} - {self.barangay}" 



