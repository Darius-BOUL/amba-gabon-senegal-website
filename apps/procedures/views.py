from django.shortcuts import render, get_object_or_404
from .models import Procedure
import html
import re



def procedures_home(request):
    return render(request, "procedures/procedures_home.html")

def procedure_detail(request, slug):
    procedure = get_object_or_404(Procedure, slug=slug, is_published=True)


 

    # 1. Déséchapper les entités HTML (&eacute; → é)
    content = html.unescape(procedure.content)

    # 2. Supprimer toutes les balises HTML (<p>, <br>, etc.)
    content = re.sub(r'<[^>]+>', '', content)

    procedure.content = content

    return render(request, "procedures/procedure_detail.html", {
        "procedure": procedure
    })
