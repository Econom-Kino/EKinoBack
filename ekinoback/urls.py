from django.urls import path
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger docs view setup
schema_view = get_schema_view(
   openapi.Info(
      title="EKino API",
      default_version='v1.56',
      description="Lviv cinema aggregator"
   ),
   public=True
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0)),

    # Movies urls
    path('movies/', getMoviesList),
    path('movies/search/', getMovieByName),
    path('movies/announces/', getAnnounces),
    path('movies/inRolling/', inRolling),
    path('movies/getToday/', getTodayMovies),
    path('movies/date/<int:year>/<int:day>/<int:month>/', getMoviesByDate),
    path('movies/place_id/<str:place_id>/', getMoviesByCinema),
    path('movies/id/<int:pk>/', getMovieItem),

    # Cinemas urls
    path('cinemas/', getCinemasList),
    path('cinemas/movie_id/<int:pk>/', getCinemasByMovie),
    path('cinemas/place_id/<str:place_id>/', getCinemaItem),

    # Genres urls
    path('genres/', getGenresList),
    path('genres/id/<int:pk>/', getGenreItem), 

    # Sessions urls
    path('sessions/', getSessionsList),
    path('sessions/movie/<int:pk>/', getSessionsByMovie),
    path('sessions/cinema/<str:place_id>/', getSessionsByCinema),    
    path('sessions/id/<int:pk>/', getSessionItem),

    # Cinema images urls
    path('cinema-images/', getCinemaImagesList),
    path('cinema-images/cinema/<str:place_id>/', getImagesByCinema),
    path('cinema-images/id/<int:pk>/', getCinemaImageItem),

    # Actors urls
    path('actors/', getActorsList),
    path('actors/id/<int:pk>/', getActorItem),

    # Studios urls
    path('studios/', getStudiosList),
    path('studios/id/<int:pk>/', getStudioItem),
]