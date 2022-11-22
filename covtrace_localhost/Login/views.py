from django.shortcuts import render

# Create your views here. 

def User_login(request):
    return render(request, "html_file/login.html", {})