from django.db import models
from django.conf import settings
from apps.articulos.models import Noticia  # Ajusta la ruta según tu estructura

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    # Campos para la IA:
    sentimiento = models.CharField(max_length=20, blank=True)  # 'positivo', 'negativo' o 'neutral'
    etiquetado_spam = models.BooleanField(default=False)
    reaction_emoji = models.CharField(max_length=10, blank=True)  # Guardaremos el emoji asignado

    def __str__(self):
        return f'Comentario de {self.usuario} en {self.noticia}'
