from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.templatetags.static import static
from .models import Character, House, Season

# Vista para la página de inicio
class HomePageView(TemplateView):
    template_name = 'appJuegoDeTronos/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        houses = House.objects.all()
        featured_characters = {
            house: {
                "character": house.characters.order_by('name').first(),
                "house_image_url": static(f"media/casa_{house.name.lower()}.jpg"),
                "character_image_url": static(f"media/{house.characters.order_by('name').first().name.lower().replace(' ', '_')}.jpg")
                    if house.characters.order_by('name').first() else None,
            }
            for house in houses
        }
        context['featured_characters'] = featured_characters
        return context

# Vista para la lista de personajes
class CharacterListView(ListView):
    model = Character
    template_name = 'appJuegoDeTronos/characters_list.html'
    context_object_name = 'characters_with_images'

    def get_queryset(self):
        characters = Character.objects.all().order_by('name')
        return [
            {
                "character": character,
                "image_url": static(f"media/{character.name.lower().replace(' ', '_')}.jpg")
            }
            for character in characters
        ]

# Vista para el detalle de un personaje
class CharacterDetailView(DetailView):
    model = Character
    template_name = 'appJuegoDeTronos/character_detail.html'
    context_object_name = 'character'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        character = self.get_object()
        character_image_url = static(f"media/{character.name.lower().replace(' ', '_')}.jpg")
        
        house_data = None
        if character.house:
            house_data = {
                "name": character.house.name,
                "description": character.house.description,
                "image_url": static(f"media/casa_{character.house.name.lower().replace(' ', '_')}.jpg")
            }

        seasons = character.seasons.all()
        context.update({
            'character_image_url': character_image_url,
            'house_data': house_data,
            'seasons': seasons
        })
        return context

# Vista para la lista de casas
class HouseListView(ListView):
    model = House
    template_name = 'appJuegoDeTronos/houses_list.html'
    context_object_name = 'houses_with_images'

    def get_queryset(self):
        houses = House.objects.all().order_by('name')
        return [
            {
                "house": house,
                "image_url": static(f"media/casa_{house.name.lower()}.jpg"),
            }
            for house in houses
        ]

# Vista para el detalle de una casa
class HouseDetailView(DetailView):
    model = House
    template_name = 'appJuegoDeTronos/house_detail.html'
    context_object_name = 'house'

# Vista para la lista de temporadas
class SeasonListView(ListView):
    model = Season
    template_name = 'appJuegoDeTronos/seasons_list.html'
    context_object_name = 'seasons_with_images'

    def get_queryset(self):
        seasons = Season.objects.all().order_by('number')
        return [
            {
                "season": season,
                "image_url": static(f"media/season_{season.number}.jpg"),
            }
            for season in seasons
        ]

# Vista para el detalle de una temporada
class SeasonDetailView(DetailView):
    model = Season
    template_name = 'appJuegoDeTronos/season_detail.html'
    context_object_name = 'season'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        season = self.get_object()
        characters = Character.objects.filter(seasons=season)  # Obtener personajes de la temporada
        context['characters'] = characters
        return context
