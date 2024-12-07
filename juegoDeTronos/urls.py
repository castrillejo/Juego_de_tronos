from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

# Definir las rutas principales
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Agregar soporte para idiomas con i18n_patterns
urlpatterns += i18n_patterns(
    path('', include('appJuegoDeTronos.urls')),  # Incluye las rutas de la app
)

# Soporte para archivos estáticos y multimedia en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





