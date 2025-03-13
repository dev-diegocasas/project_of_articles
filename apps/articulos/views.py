from django.shortcuts import render, get_object_or_404
from .models import Noticia
import os
from django.conf import settings
from django.shortcuts import render

def home(request):
    return render(request, 'layouts/base.html') 

def global_settings(request):
    return {'MEDIA_URL': settings.MEDIA_URL}


def lista_noticias(request):
    noticias = Noticia.objects.filter(publicada=True).order_by('-fecha_publicacion')
    return render(request, 'articulos/lista_noticias.html', {'noticias': noticias})

#def detalle_noticia(request, id):
    #noticia = get_object_or_404(Noticia, id=id, publicada=True)
   # return render(request, 'articulos/detalle_noticia.html', {'noticia': noticia})

def detalle_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id, publicada=True)
    # Cargar todos los comentarios relacionados, ordenados por fecha de publicación descendente.
    comentarios = noticia.comentarios.order_by('-fecha_publicacion')
    return render(request, 'articulos/detalle_noticia.html', {
        'noticia': noticia,
        'comentarios': comentarios,
    })



def galeria_noticias(request):
    """Muestra todas las imágenes dentro de /media/noticias/ como una galería."""
    media_path = os.path.join(settings.MEDIA_ROOT, 'noticias')  # Ruta física
    archivos = []

    if os.path.exists(media_path):  # Verificar que la carpeta existe
        archivos = [
            f"{archivo}" for archivo in os.listdir(media_path)
            if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
        ]  # Filtrar solo imágenes

    return render(request, 'articulos/noticias.html', {'archivos': archivos})


