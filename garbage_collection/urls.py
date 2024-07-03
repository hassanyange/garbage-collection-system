
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('collection_system.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 





admin.site.site_header = "MUNICIPAL GARBAGE COLLECTION SYSTEM"
admin.site.index_title = "Welcome to Municipal Garbage Collection System"
admin.site.site_title = "Collection System"
