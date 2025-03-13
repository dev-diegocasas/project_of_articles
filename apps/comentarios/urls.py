from django.urls import path
from . import views

urlpatterns = [
    path('agregar/<int:noticia_id>/', views.agregar_comentario, name='agregar_comentario'),
]
