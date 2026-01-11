from django.urls import path
from .views import news_home

app_name = "news"

urlpatterns = [
    path("", news_home, name="home"),
]