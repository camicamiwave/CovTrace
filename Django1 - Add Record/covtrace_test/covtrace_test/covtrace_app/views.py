from django.shortcuts import render 
from .forms import PatientForm

def say_hello(request): 
    return render(request, 'hello.html', { 'name': 'John'})

#localhost - http://127.0.0.1:8000/covtrace_app/join/
#admin - http://127.0.0.1:8000/admin

def Add_Patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'add_record.html', {}) 

    else:
        return render(request, 'add_record.html', {}) 
