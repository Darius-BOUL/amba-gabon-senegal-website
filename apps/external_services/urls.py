from django.urls import path
from .views import external_services_home

app_name = "external_services"

urlpatterns = [
    path("", external_services_home, name="home"),
]
