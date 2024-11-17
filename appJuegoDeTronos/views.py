from django.shortcuts import render, get_object_or_404
from .models import Character, House, Season

# Vista para la página de inicio
def homepage(request):
    houses = House.objects.all()
    # Seleccionamos un personaje destacado por casa
    featured_characters = {house: house.characters.order_by('name').first() for house in houses}
    return render(request, 'appJuegoDeTronos/homepage.html', {'featured_characters': featured_characters})

# Vista para la lista de personajes
def characters_list(request):
    characters = Character.objects.all().order_by('name')  # Listar personajes alfabéticamente
    return render(request, 'appJuegoDeTronos/characters_list.html', {'characters': characters})

# Vista para el detalle de un personaje
def character_detail(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    return render(request, 'appJuegoDeTronos/character_detail.html', {'character': character})

# Vista para la lista de casas
def houses_list(request):
    houses = House.objects.all().order_by('name')  # Listar casas alfabéticamente
    return render(request, 'appJuegoDeTronos/houses_list.html', {'houses': houses})

# Vista para el detalle de una casa
def house_detail(request, house_id):
    house = get_object_or_404(House, id=house_id)
    return render(request, 'appJuegoDeTronos/house_detail.html', {'house': house})

# Vista para la lista de temporadas
def seasons_list(request):
    seasons = Season.objects.all().order_by('number')  # Listar temporadas en orden numérico
    return render(request, 'appJuegoDeTronos/seasons_list.html', {'seasons': seasons})

# Vista para el detalle de una temporada
def season_detail(request, season_id):
    season = get_object_or_404(Season, id=season_id)
    return render(request, 'appJuegoDeTronos/season_detail.html', {'season': season})
