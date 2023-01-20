from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant
# Create your views here.

def create(request):
    place = Place(name="Lugar 1", addres="Calle Demo")
    place.save()

    restaurant = Restaurant(place=place, number_of_employes=8)
    restaurant.save()    
    # Crear elementos
    return HttpResponse(restaurant.place.name)