from django.shortcuts import render

def News(request):  
    return render(request, "news_urls/news_about_covid.html", {})