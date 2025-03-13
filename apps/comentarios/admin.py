from django.contrib import admin
from .models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('noticia', 'usuario', 'sentimiento', 'etiquetado_spam', 'reaction_emoji', 'fecha_publicacion')
    list_filter = ('etiquetado_spam', 'sentimiento', 'fecha_publicacion')
    search_fields = ('contenido',)
