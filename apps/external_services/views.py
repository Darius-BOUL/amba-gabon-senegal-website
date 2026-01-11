from django.shortcuts import render

def external_services_home(request):
    return render(request, "external_services/external_services_home.html")
