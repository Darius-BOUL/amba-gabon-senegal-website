from django.urls import path
from .views import consular_home

app_name = "consular"

urlpatterns = [
    path("", consular_home, name="home"),
]
