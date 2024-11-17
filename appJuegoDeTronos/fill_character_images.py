from appJuegoDeTronos.models import Character
import os

# Ruta base ajustada para incluir appJuegoDeTronos/static/media
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_MEDIA_PATH = os.path.normpath(os.path.join(BASE_DIR, "appJuegoDeTronos/static/media/"))

def fill_images():
    characters = Character.objects.all()

    for character in characters:
        # Generar el nombre del archivo basado en el nombre del personaje
        filename = character.name.lower().replace(" ", "_") + ".jpg"
        file_path = os.path.normpath(os.path.join(STATIC_MEDIA_PATH, filename))

        print(f"Buscando archivo: {file_path}")  # Debug: imprimir la ruta completa

        # Verificar si el archivo existe
        if os.path.isfile(file_path):
            # Guardar la ruta relativa en el campo de imagen del personaje
            character.image = f"media/{filename}"
            character.save()
            print(f"Imagen asignada a: {character.name}")
        else:
            print(f"Imagen no encontrada para: {character.name} (archivo {filename})")
