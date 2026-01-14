from django.urls import path
from .views import news_home, news_detail

app_name = "news"

urlpatterns = [
    path("", news_home, name="home"),
     path('<slug:slug>/', news_detail, name='detail'),
]