"""
DJango app urls.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from api.urls import router


urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
