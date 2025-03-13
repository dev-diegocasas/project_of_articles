from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.articulos.urls')), 
    path('noticias/', include('apps.articulos.urls')),
    path('comentarios/', include('apps.comentarios.urls')),
    path('media/noticias/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT + '/noticias'}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
