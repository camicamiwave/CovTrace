from django.contrib import admin
from Home.models import Total_Positive_Patient, Total_Recovered_Patient, Total_Died_Patient, New_Total_Number_Positive_Patient, New_Total_Number_Recovered_Patient, New_Total_Number_Died_Patient


admin.site.register(Total_Positive_Patient)
admin.site.register(Total_Recovered_Patient)
admin.site.register(Total_Died_Patient)
admin.site.register(New_Total_Number_Positive_Patient)
admin.site.register(New_Total_Number_Recovered_Patient)
admin.site.register(New_Total_Number_Died_Patient)