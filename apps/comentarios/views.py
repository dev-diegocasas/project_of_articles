from django.shortcuts import render, get_object_or_404, redirect
from apps.articulos.models import Noticia
from .forms import ComentarioForm
from .utils import analizar_sentimiento, detectar_spam, asignar_reaccion

def agregar_comentario(request, noticia_id):
    """Crea un comentario y aplica análisis de sentimiento y detección de spam básico."""
    noticia = get_object_or_404(Noticia, id=noticia_id)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.noticia = noticia
            if request.user.is_authenticated:
                comentario.usuario = request.user

            # Análisis básico con funciones definidas en utils.py
            sentimiento = analizar_sentimiento(comentario.contenido)
            es_spam = detectar_spam(comentario.contenido)
            emoji = asignar_reaccion(sentimiento, es_spam)

            comentario.sentimiento = sentimiento
            comentario.etiquetado_spam = es_spam
            comentario.reaction_emoji = emoji
            comentario.save()

            return redirect('detalle_noticia', id=noticia.id)
    else:
        form = ComentarioForm()

    return render(request, 'agregar_comentario.html', {
        'form': form,
        'noticia': noticia
    })
