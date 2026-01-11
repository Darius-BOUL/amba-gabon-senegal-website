from django.urls import path
from .views import institution_home

app_name = "institution"

urlpatterns = [
    path("", institution_home, name="home"),
]
