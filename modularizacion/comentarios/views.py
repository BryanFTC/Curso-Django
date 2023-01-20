from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.

def test(request):
    return HttpResponse("Funciona Correctamente")

def create(request):
    # comment = Comment(name="Juanjo", score=5, comments="Este es un comentario")
    # comment.save()
    # comment = Comment.objects.create(name="Alex")
    return HttpResponse("Ruta para probar la creacion de modelos")

def delete(request):
    # comment = Comment.objects.get(id=2)
    # comment.delete()
    # Comment.objects.filter(id=3).delete()
    return HttpResponse("Ruta para probar borrados")