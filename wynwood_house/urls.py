from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path('', include('properties.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
