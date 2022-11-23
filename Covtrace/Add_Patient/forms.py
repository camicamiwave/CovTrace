from .models import Patient
from django.forms import ModelForm

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'birthday', 'age', 'gender', 'barangay', 'status', 'date_admitted']

