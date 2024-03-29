from django.contrib import admin
from django.urls import path, include
# for the media files to show up in the front end
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('listings/', include('listings.urls')),
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
