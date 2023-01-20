from django.shortcuts import render
from .forms import CommentForm, ContactForm
from django.http import HttpResponse


def form(request):
    comment_form = CommentForm({'name': 'Juanjo', 'url': 'http://openb.com', 'comment': 'Comentario'})
    return render(request, 'form.html', {'comment_form': comment_form})


def goal(request):
    
    if request.method != 'POST':
        return HttpResponse('Metodo no permitido')

    return HttpResponse(request.POST['name'])

def widget(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'form': form})

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #Aqui iran todas las acciones a realizar cuando los datos son correctos
            return HttpResponse("Valido")
        else:
            #Aqui comunicamos al usario que los datos no son validos
            return render(request, 'widget.html', {'form': form})