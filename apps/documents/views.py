from django.shortcuts import render

def documents_home(request):
    return render(request, "documents/documents_home.html")
