from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from django.templatetags.static import static
from .models import Character, House, Season
from django.utils.translation import get_language
from django.http import JsonResponse
from django.contrib import messages
import os
from django.conf import settings
from .forms import CharacterForm

from django.views.generic.edit import FormView
from django.urls import reverse_lazy

class CharacterInfoView(View):
    def get(self, request, character_id):
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
                    "character_image_url": self.get_character_image_url(character) if character else None,
                }
        else:
            for house in houses:
                character = house.characters.order_by('name').first()
                featured_characters[house] = {
                    "character": character,
                    "house_image_url": static(f"media/casa_{house.name.lower()}.jpg"),
                    "character_image_url": self.get_character_image_url(character) if character else None,
                }

        context['houses'] = houses
        context['featured_characters'] = featured_characters
        return context

    def get_character_image_url(self, character):
        """
        Busca la imagen del personaje tanto en static/media como en media/.
        """
        if not character:
            return None
        
        static_path = os.path.join(settings.BASE_DIR, 'appJuegoDeTronos', 'static', 'media', f"{character.name.lower().replace(' ', '_')}.jpg")
        media_path = os.path.join(settings.MEDIA_ROOT, f"{character.name.lower().replace(' ', '_')}.jpg")

        if os.path.exists(static_path):
            return static(f"media/{character.name.lower().replace(' ', '_')}.jpg")

        if os.path.exists(media_path):
            return f"{settings.MEDIA_URL}{character.name.lower().replace(' ', '_')}.jpg"

        return None

# Vista para la lista de personajes
class CharacterListView(ListView):
    model = Character
    template_name = 'appJuegoDeTronos/characters_list.html'
    context_object_name = 'characters_with_images'

    def get_queryset(self):
        def get_image_url(character):
            static_path = os.path.join(settings.BASE_DIR, 'appJuegoDeTronos', 'static', 'media', f"{character.name.lower().replace(' ', '_')}.jpg")
            media_path = os.path.join(settings.BASE_DIR, 'media', f"{character.name.lower().replace(' ', '_')}.jpg")

            if os.path.exists(static_path):
                return static(f"media/{character.name.lower().replace(' ', '_')}.jpg")

            if os.path.exists(media_path):
                return f"/media/{character.name.lower().replace(' ', '_')}.jpg"

            return None

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

        static_path = os.path.join(settings.BASE_DIR, 'appJuegoDeTronos', 'static', 'media', f"{character.name.lower().replace(' ', '_')}.jpg")
        media_path = os.path.join(settings.MEDIA_ROOT, f"{character.name.lower().replace(' ', '_')}.jpg")

        if os.path.exists(static_path):
            character_image_url = static(f"media/{character.name.lower().replace(' ', '_')}.jpg")
        elif os.path.exists(media_path):
            character_image_url = f"{settings.MEDIA_URL}{character.name.lower().replace(' ', '_')}.jpg"
        else:
            character_image_url = None

        house_data = None
        if character.house:
            house_static_path = os.path.join(settings.BASE_DIR, 'appJuegoDeTronos', 'static', 'media', f"casa_{character.house.name.lower().replace(' ', '_')}.jpg")
            house_media_path = os.path.join(settings.MEDIA_ROOT, f"casa_{character.house.name.lower().replace(' ', '_')}.jpg")

            if os.path.exists(house_static_path):
                house_image_url = static(f"media/casa_{character.house.name.lower().replace(' ', '_')}.jpg")
            elif os.path.exists(house_media_path):
                house_image_url = f"{settings.MEDIA_URL}casa_{character.house.name.lower().replace(' ', '_')}.jpg"
            else:
                house_image_url = None

            house_data = {
                "id": character.house.id,
                "name": character.house.name,
                "description": character.house.description,
                "image_url": house_image_url
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
        characters = Character.objects.filter(seasons=season)
        context['characters'] = characters
        return context

class AddCharacterView(FormView):
    template_name = 'appJuegoDeTronos/add_character.html'
    form_class = CharacterForm
    success_url = reverse_lazy('characters_list')

    def form_valid(self, form):
        character = form.save(commit=False)
        character.save()
        form.save_m2m()
        messages.success(self.request, "El personaje ha sido añadido con éxito.")
        return super().form_valid(form)