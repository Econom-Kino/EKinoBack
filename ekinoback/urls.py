from django.urls import path
from .views import *
from .paramViews import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger docs view setup
schema_view = get_schema_view(
   openapi.Info(
      title="EKino API",
      default_version='v1.70',
      description="Lviv cinema aggregator"
   ),
   public=True
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0)),

    # Movies urls
    path('movies', getMoviesList),
    path('movies/search', getMovieByName),
    path('movies/announces', getAnnounces),
    path('movies/in-rolling', inRolling),
    path('movies/today', getTodayMovies),
    path('movies/date/<int:year>/<int:day>/<int:month>', getMoviesByDate),
    path('movies/<int:pk>', getMovieItem),
    path('movies/<int:pk>/cinemas', getCinemasByMovie),
    path('movies/<int:pk>/sessions', getSessionsByMovie),
    path('movies/<int:pk>/date/<int:year>/<int:day>/<int:month>/sessions', getSessionsByMovieAndDate),

    # Cinemas urls
    path('cinemas', getCinemasList),
    path('cinemas/<str:place_id>/movies', getMoviesByCinema),
    path('cinemas/<str:place_id>', getCinemaItem),
    path('cinemas/<str:place_id>/cinema-images', getImagesByCinema),
    path('cinemas/<str:place_id>/sessions', getSessionsByCinema),
    path('cinemas/<str:place_id>/movies/<int:pk>/sessions', getSessionsByBoth), 

    # Genres urls
    path('genres', getGenresList),
    path('genres/<int:pk>', getGenreItem), 

    # Sessions urls
    path('sessions', getSessionsList),   
    path('sessions/<int:pk>', getSessionItem),

    # Cinema images urls
    path('cinema-images', getCinemaImagesList),
    path('cinema-images/<int:pk>', getCinemaImageItem),

    # Actors urls
    path('actors', getActorsList),
    path('actors/<int:pk>', getActorItem),

    # Studios urls
    path('studios', getStudiosList),
    path('studios/<int:pk>', getStudioItem),

    #Special urls
    path('clear/sessions', clearUselessSessions),
    path('clear/movies', clearUselessMovies),
]