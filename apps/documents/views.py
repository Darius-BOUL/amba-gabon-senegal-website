from django.shortcuts import render
from .models import Document

def documents_home(request):
    documents = Document.objects.all()
    return render(request, "documents/documents_home.html", {"documents": documents})
