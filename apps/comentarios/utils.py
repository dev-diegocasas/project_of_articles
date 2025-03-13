from textblob import TextBlob

from textblob import TextBlob

from textblob import TextBlob
import re

def analizar_sentimiento(texto):
    # Convertir el texto a minúsculas para una mejor comparación
    texto = texto.lower()

    # Lista de palabras clave para mejorar la detección
    palabras_positivas = ["me encanta", "guapo", "hermoso", "adorable", "lindo", "genial", "asombroso", "bello"]
    palabras_negativas = ["feo", "miedo", "horrible", "asqueroso", "odio", "muere", "estúpido", "tonto"]

    # Detectar palabras clave en el texto
    if any(palabra in texto for palabra in palabras_positivas):
        return 'positivo'
    if any(palabra in texto for palabra in palabras_negativas):
        return 'negativo'

    # Analizar sentimiento con TextBlob
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity

    # Ajustar los umbrales para mejorar la precisión
    if polaridad > 0.2:
        return 'positivo'
    elif polaridad < -0.2:
        return 'negativo'
    else:
        return 'neutral'


def detectar_spam(texto):
    """
    Detecta si un comentario es spam basado en lenguaje ofensivo, exceso de enlaces y formato sospechoso.
    """
    palabras_prohibidas = ['esa cosa', 'basura', 'mal animal', 'apestoso', 'asqueroso', 'odioso', 'feo', 'inútil', 'plaga']
    texto_lower = texto.lower()

    # Detectar palabras ofensivas
    for palabra in palabras_prohibidas:
        if palabra in texto_lower:
            return True
    
    # Detectar exceso de enlaces
    patron_url = r"(https?:\/\/|www\.)\S+"
    if len(re.findall(patron_url, texto)) > 2:
        return True

    # Detectar abuso de mayúsculas o símbolos exagerados
    if texto.isupper() or texto.count("!") > 3 or texto.count("?") > 3:
        return True

    # Detectar mensajes demasiado cortos con palabras agresivas
    if len(texto) < 5 and any(palabra in texto_lower for palabra in palabras_prohibidas):
        return True
    
    return False

def asignar_reaccion(sentimiento, es_spam):
    """
    Retorna un emoji según el sentimiento y si es spam.
    """
    if es_spam:
        return '🚫'
    
    reacciones = {
        'positivo': '👍',
        'ligeramente positivo': '🙂',
        'neutral': '😐',
        'ligeramente negativo': '🙁',
        'negativo': '😠'
    }
    
    return reacciones.get(sentimiento, '😐') 