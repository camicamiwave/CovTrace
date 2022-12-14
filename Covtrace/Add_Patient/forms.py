from Add_Patient.models import Patient_Detail, New_Positive_Detail, Positive_Detail
from django.forms import ModelForm

class PatientForm(ModelForm):
    class Meta:
        model = Patient_Detail
        fields = ['name', 'age', 'gender', 'barangay', 'status', 'date_admitted'] 

class New_Positive_Cases_Patient(ModelForm):
    class Meta:
        model = New_Positive_Detail
        fields = ['name', 'age', 'gender', 'barangay', 'status', 'date_admitted']

class Total_Positive_Cases_Patient(ModelForm):
    class Meta:
        model = Positive_Detail
        fields = ['name', 'age', 'gender', 'barangay', 'status', 'date_admitted']