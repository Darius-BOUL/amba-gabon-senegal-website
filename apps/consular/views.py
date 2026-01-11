from django.shortcuts import render

def consular_home(request):
    return render(request, "consular/consular_home.html")
