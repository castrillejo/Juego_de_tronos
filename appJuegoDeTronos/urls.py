from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('characters/', views.characters_list, name='characters_list'),
    path('characters/<int:character_id>/', views.character_detail, name='character_detail'),
    path('houses/', views.houses_list, name='houses_list'),
    path('houses/<int:house_id>/', views.house_detail, name='house_detail'),
    path('seasons/', views.seasons_list, name='seasons_list'),
    path('seasons/<int:season_id>/', views.season_detail, name='season_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
