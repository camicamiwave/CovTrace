from django.shortcuts import render

def About_Us_Page(request):
    return render(request, "aboutus_html/about_us.html", {})