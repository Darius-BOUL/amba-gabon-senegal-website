from django.shortcuts import render

def mentions_legales(request):
    return render(request, "legal/mentions_legales.html")

def contact(request):
    return render(request, "legal/contact.html")


