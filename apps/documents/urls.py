from django.urls import path
from .views import documents_home

app_name = "documents"

urlpatterns = [
    path("", documents_home, name="home"),
]
