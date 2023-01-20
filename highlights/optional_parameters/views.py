from django.shortcuts import render

# Create your views here.

def optional(request, name = 'Nombre por defecto'):
    return render(request, 'optional.html', {'name': name})
