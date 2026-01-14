from django.urls import path
from .views import mentions_legales, contact

app_name = "legal"

urlpatterns = [
    path("mentions-legales/", mentions_legales, name="mentions"),
    path("contact/", contact, name="contact"),
]
