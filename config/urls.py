from django.contrib import admin
from django.urls import path, include
from apps.core.views import home

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("apps.pages.urls")),
    path("ambassade/", include("apps.institution.urls")),
    path("services/", include("apps.consular.urls")),
    path("procedures/", include("apps.procedures.urls")),
    path("actualites/", include("apps.news.urls")),
    path("documents/", include("apps.documents.urls")),
    path("services-externes/", include("apps.external_services.urls")),
    path("legal/", include("apps.legal.urls")),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)