from django.shortcuts import render

def institution_home(request):
    return render(request, "institution/institution_home.html")
