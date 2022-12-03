from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainApp.urls")),
    path('news/', include("mainApp.urls")),
    path('about/', include("mainApp.urls")),
    path('service/', include("service.urls")),
    path('service/catalog-ap/', include("flats.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
