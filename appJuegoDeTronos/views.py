from django.shortcuts import render, get_object_or_404
from .models import Character, House, Season
from django.templatetags.static import static
# Vista para la página de inicio
from django.conf import settings

def homepage(request):
    houses = House.objects.all()
    featured_characters = {
        house: {
            "character": house.characters.order_by('name').first(),
            # Construir URL de la imagen de la casa
            "house_image_url": static(f"media/casa_{house.name.lower()}.jpg"),
            # Construir URL de la imagen del personaje si existe
            "character_image_url": static(f"media/{house.characters.order_by('name').first().name.lower().replace(' ', '_')}.jpg")
                                   if house.characters.order_by('name').first() else None,
        }
        for house in houses
    }
    return render(request, 'appJuegoDeTronos/homepage.html', {'featured_characters': featured_characters})
# Vista para la lista de personajes
def characters_list(request):
    characters = Character.objects.all().order_by('name')  # Listar personajes alfabéticamente
    return render(request, 'appJuegoDeTronos/characters_list.html', {'characters': characters})

# Vista para el detalle de un personaje
def character_detail(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    # Generar la URL de la imagen del personaje
    character_image_url = static(f"media/{character.name.lower().replace(' ', '_')}.jpg")
    return render(request, 'appJuegoDeTronos/character_detail.html', {
        'character': character,
        'character_image_url': character_image_url
    })

def houses_list(request):
    houses = House.objects.all().order_by('name')  # Listar casas alfabéticamente
    houses_with_images = [
        {
            "house": house,
            "image_url": static(f"media/casa_{house.name.lower()}.jpg"),  # Ruta de la imagen de la casa
        }
        for house in houses
    ]
    return render(request, 'appJuegoDeTronos/houses_list.html', {'houses_with_images': houses_with_images})
# Vista para el detalle de una casa
def house_detail(request, house_id):
    house = get_object_or_404(House, id=house_id)
    return render(request, 'appJuegoDeTronos/house_detail.html', {'house': house})

# Vista para la lista de temporadas

def seasons_list(request):
    seasons = Season.objects.all().order_by('number')  # Listar temporadas en orden numérico
    seasons_with_images = [
        {
            "season": season,
            "image_url": static(f"media/season_{season.number}.jpg"),  # Ruta de la imagen de la temporada
        }
        for season in seasons
    ]
    return render(request, 'appJuegoDeTronos/seasons_list.html', {'seasons_with_images': seasons_with_images})
# Vista para el detalle de una temporada
def season_detail(request, season_id):
    season = Season.objects.get(id=season_id)
    characters = Character.objects.filter(seasons=season)  # Obtener personajes relacionados con la temporada
    return render(request, 'appJuegoDeTronos/season_detail.html', {
        'season': season,
        'characters': characters
    })