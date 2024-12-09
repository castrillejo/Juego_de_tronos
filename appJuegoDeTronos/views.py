from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.templatetags.static import static
from .models import Character, House, Season
from django.utils.translation import get_language
from django.http import HttpResponse
from .forms import CharacterForm 
from django.http import JsonResponse 
from django.contrib import messages
import os
from django.conf import settings


def character_info(request, character_id):
    try:
        character = Character.objects.get(id=character_id)
        return JsonResponse({'is_alive': character.is_alive})
    except Character.DoesNotExist:
        return JsonResponse({'error': 'Character not found'}, status=404)
    
# Vista para la página de inicio
class HomePageView(TemplateView):
    template_name = 'appJuegoDeTronos/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LANGUAGES'] = settings.LANGUAGES 
        context['LANGUAGE_CODE'] = get_language()  
        house_filter = self.request.GET.get('house', None)
        houses = House.objects.all()

        featured_characters = {}
        if house_filter:
            selected_house = houses.filter(name=house_filter).first()
            if selected_house:
                character = selected_house.characters.order_by('name').first()
                featured_characters[selected_house] = {
                    "character": character,
                    "house_image_url": static(f"media/casa_{selected_house.name.lower()}.jpg"),
                    "character_image_url": static(f"media/{character.name.lower().replace(' ', '_')}.jpg")
                    if character else None,
                }
        else:
            for house in houses:
                character = house.characters.order_by('name').first()
                featured_characters[house] = {
                    "character": character,
                    "house_image_url": static(f"media/casa_{house.name.lower()}.jpg"),
                    "character_image_url": static(f"media/{character.name.lower().replace(' ', '_')}.jpg")
                    if character else None,
                }

        context['houses'] = houses
        context['featured_characters'] = featured_characters
        return context




# Vista para la lista de personajes
class CharacterListView(ListView):
    model = Character
    template_name = 'appJuegoDeTronos/characters_list.html'
    context_object_name = 'characters_with_images'

    def get_queryset(self):
        def get_image_url(character):
            static_path = os.path.join(settings.BASE_DIR, 'appJuegoDeTronos', 'static', 'media', f"{character.name.lower().replace(' ', '_')}.jpg")
            media_path = os.path.join(settings.BASE_DIR, 'media', f"{character.name.lower().replace(' ', '_')}.jpg")

            # Imprime información detallada para depuración
            print(f"[Checking Static Path] {character.name}: {static_path} - Exists: {os.path.exists(static_path)}")
            print(f"[Checking Media Path] {character.name}: {media_path} - Exists: {os.path.exists(media_path)}")

            if os.path.exists(static_path):
                url = static(f"media/{character.name.lower().replace(' ', '_')}.jpg")
                print(f"[Static Found] {character.name}: {url}")
                return url

            if os.path.exists(media_path):
                url = f"/media/{character.name.lower().replace(' ', '_')}.jpg"
                print(f"[Media Found] {character.name}: {url}")
                return url

            print(f"[No Image Found] {character.name}")
            return None

        # Obtener todos los personajes y construir el queryset con la URL de la imagen
        return [
            {
                "character": character,
                "image_url": get_image_url(character)
            }
            for character in Character.objects.all().order_by('name')
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
                "id":character.house.id,
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


def add_character_form(request):
    if request.method == "POST":
        form = CharacterForm(request.POST, request.FILES)
        if form.is_valid():
            character = form.save(commit=False)
            character.save()
            form.save_m2m()
            messages.success(request, "El personaje ha sido añadido con éxito.")  # Mensaje de éxito
            return redirect('characters_list')
    else:
        form = CharacterForm()

    return render(request, 'appJuegoDeTronos/add_character.html', {'form': form})