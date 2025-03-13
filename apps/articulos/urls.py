from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.urls import path, re_path
from apps.articulos.views import galeria_noticias

urlpatterns = [
    path('', views.lista_noticias, name='lista_noticias'),
    path('<int:id>/', views.detalle_noticia, name='detalle_noticia'),
    re_path(r'^media/noticias/$', galeria_noticias, name='galeria_noticias'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)