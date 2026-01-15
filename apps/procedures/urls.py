from django.urls import path
from .views import procedures_home, procedure_detail

app_name = "procedures"

urlpatterns = [
    path("", procedures_home, name="home"),
    path("<slug:slug>/", procedure_detail, name="detail"),
]