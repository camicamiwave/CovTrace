from django.contrib import admin
from Home.models import New_Total_Number_Recovered_Patient, Total_Number_Recovered_Patient, New_Total_Number_Positive_Patient, Total_Number_Positive_Patient, Patient_List, New_Total_Number_Died_Patient, Total_Number_Died_Patient

admin.site.register(New_Total_Number_Recovered_Patient)
admin.site.register(Total_Number_Recovered_Patient)
admin.site.register(New_Total_Number_Positive_Patient)
admin.site.register(Total_Number_Positive_Patient)
admin.site.register(New_Total_Number_Died_Patient)
admin.site.register(Total_Number_Died_Patient)
admin.site.register(Patient_List)