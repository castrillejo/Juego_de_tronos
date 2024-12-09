from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import character_info

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'), 
    path('characters/', views.CharacterListView.as_view(), name='characters_list'),  
    path('characters/<int:pk>/', views.CharacterDetailView.as_view(), name='character_detail'),  
    path('houses/', views.HouseListView.as_view(), name='houses_list'),  
    path('houses/<int:pk>/', views.HouseDetailView.as_view(), name='house_detail'),  
    path('seasons/', views.SeasonListView.as_view(), name='seasons_list'),  
    path('seasons/<int:pk>/', views.SeasonDetailView.as_view(), name='season_detail'),  
    path('add_character/', views.add_character_form, name='add_character'),
    path('api/character-info/<int:character_id>/', views.character_info, name='character_info')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)