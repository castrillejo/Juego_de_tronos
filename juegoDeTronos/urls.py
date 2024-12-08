from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # Rutas no relacionadas con el idioma, si las hay
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('appJuegoDeTronos.urls')),
)
