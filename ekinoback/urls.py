from django.urls import path
from .views import *

urlpatterns = [
    path('movies/', getMoviesList),
    path('movies/place_id/<str:place_id>', getMoviesByCinema)
    path('movies/id/<int:pk>/', getMovieItem),
    path('cinemas/', getCinemaList),
    path('cinemas/place_id/<str:place_id>/', getCinemaItem),
    path('genres/', getGenreList),
    path('genres/id/<int:pk>/', getGenreItem), 
    path('sessions/', getSessionList),
    path('sessions/movie/<int:pk>/', getSessionByMovie),
    path('sessions/cinema/<str:place_id>/', getSessionByCinema),    
    path('sessions/id/<int:pk>/', getSessionItem),
    path('cinema-images/', getCinemaImagesList),
    path('cinema-images/cinema/<str:place_id>/', getImageByCinema),
    path('cinema-images/id/<int:pk>/', getCinemaImageItem),
    path('actors/', getActorsList),
    path('actors/id/<int:pk>/', getActorItem),
    path('studios/', getStudiosList),
    path('studios/id/<int:pk>/', getStudioItem),
]