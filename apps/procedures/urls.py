from django.urls import path
from .views import procedures_home

app_name = "procedures"

urlpatterns = [
    path("", procedures_home, name="home"),
]
