from django.contrib import admin
from Add_Patient.models import Patient_Detail, Positive_Detail, Recovered_Detail, Death_Detail, New_Death_Detail, New_Positive_Detail, New_Recovered_Detail

admin.site.register(Patient_Detail) 
admin.site.register(Positive_Detail)
admin.site.register(Recovered_Detail) 
admin.site.register(Death_Detail) 
admin.site.register(New_Death_Detail) 
admin.site.register(New_Positive_Detail) 
admin.site.register(New_Recovered_Detail) 