from django.contrib import admin
from django.urls import path, include
from apps.core.views import home


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("ambassade/", include("apps.institution.urls")),
    path("services/", include("apps.consular.urls")),
    path("procedures/", include("apps.procedures.urls")),
    path("actualites/", include("apps.news.urls")),
    path("documents/", include("apps.documents.urls")),
    path("services-externes/", include("apps.external_services.urls")),
]
