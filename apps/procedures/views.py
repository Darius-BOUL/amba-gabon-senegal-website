from django.shortcuts import render

def procedures_home(request):
    return render(request, "procedures/procedures_home.html")
