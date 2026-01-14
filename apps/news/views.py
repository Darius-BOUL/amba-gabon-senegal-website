from django.shortcuts import render
from .models import News
from django.shortcuts import render, get_object_or_404
import html
import re



def news_home(request):
    news = News.objects.filter(is_published=True)
    return render(request, "news/news_home.html", {"news_list": news})


def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)

    # 1. Déséchapper les entités HTML (&eacute; → é)
    content = html.unescape(news_item.content)

    # 2. Supprimer toutes les balises HTML (<p>, <br>, etc.)
    content = re.sub(r'<[^>]+>', '', content)

    news_item.content = content

    return render(request, "news/news_detail.html", {
        "news": news_item
    })