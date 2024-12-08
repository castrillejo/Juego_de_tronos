from django.core.management.base import BaseCommand
from appJuegoDeTronos.models import Character

class Command(BaseCommand):
    help = "Actualizar el estado (vivo o muerto) de los personajes en la base de datos"

    def handle(self, *args, **kwargs):
        # Diccionario con los estados de los personajes
        character_status = {
            "Jon Snow": True,
            "Arya Stark": True,
            "Sansa Stark": True,
            "Tyrion Lannister": True,
            "Jaime Lannister": False,
            "Cersei Lannister": False,
            "Daenerys Targaryen": False,
            "Jorah Mormont": False,
            "Robert Baratheon": False,
            "Stannis Baratheon": False,
            "Theon Greyjoy": False,
            "Margaery Tyrell": False,
            "Oberyn Martell": False,
            "Bran Stark": True,
            "Sandor Clegane": True,
            "Petyr Baelish": False,
            "Brienne of Tarth": True,
            "Khal Drogo": False,
            "Samwell Tarly": True,
            "Gendry": True,
            "Melisandre": False,
            "Varys": False,
            "Ygritte": False,
            "Tormund Giantsbane": True,
            "Ellaria Sand": False,
            "Ramsay Bolton": False,
            "Roose Bolton": False,
            "Hodor": False,
            "Joffrey Baratheon": False,
            "Tommen Baratheon": False,
            "Daario Naharis": True,
            "Missandei": False,
            "Grey Worm": True,
            "Euron Greyjoy": False,
            "Balon Greyjoy": False,
            "Yara Greyjoy": True,
            "Barristan Selmy": False,
            "Shae": False,
            "Lyanna Mormont": False,
            "Jojen Reed": False,
            "Meera Reed": True,
            "Rickon Stark": False,
            "Maester Aemon": False,
            "Gilly": True,
            "Grenn": False,
            "Yoren": False,
            "Lysa Arryn": False,
            "Robin Arryn": True,
            "Hot Pie": True,
            "Osha": False,
            "Tywin Lannister": False,
            "Kevan Lannister": False,
            "Jaqen H'ghar": True,
            "Loras Tyrell": False,
            "High Sparrow": False,
            "Podrick Payne": True,
            "Qyburn": False,
            "Walder Frey": False,
            "Edmure Tully": True,
            "Beric Dondarrion": False,
            "Thoros of Myr": False,
        }

        # Actualizar personajes
        for name, is_alive in character_status.items():
            character = Character.objects.filter(name=name).first()
            if character:
                character.is_alive = is_alive
                character.save()
                self.stdout.write(self.style.SUCCESS(f"✅ {name}: {'Vivo' if is_alive else 'Muerto'}"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ Personaje no encontrado: {name}"))
