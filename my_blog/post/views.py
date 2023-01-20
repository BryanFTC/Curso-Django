from django.shortcuts import render
from .models import Author, Entry
from django.http import HttpResponse
# Create your views here.

def update(request):
    author = Author.objects.get(id=1)
    author.name = "Juanjo"
    author.email = "juanjo@demo.com"
    author.save()
    return HttpResponse("Modificado")

def queries(request):
    # Obtener todos los elementos
    authors = Author.objects.all()

    # Obtener datos filtrando por condicion
    # filtered = Author.objects.filter(email = 'amber05@example.org')

    #Obtener un unico objeto (filtrado)
    author = Author.objects.get(id=1)

    # Obtener los 10 primeros elementos
    limits = Author.objects.all()[:10]

    # Obtener 10 elementos saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

    # Obtener todos los elementos ordenados
    orders = Author.objects.all().order_by('email')

    # Obtener todos los elementos cuyo id sea menor o igual a 15
    # filtered = Author.objects.filter(id__lte=15)

    # Obtener todos los autores que contiene en su nombre la palabra yes
    filtered = Author.objects.filter(email__contains="uc")
    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author':author, 'limits': limits, 'offsets': offsets, 'orders': orders})