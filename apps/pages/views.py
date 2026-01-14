from django.shortcuts import render

def home(request):
    return render(request, "pages/landing.html")

def contact(request):
    return render(request, "pages/contact.html")