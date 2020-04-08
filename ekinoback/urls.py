from django.urls import path
from .views import get_post_movies, get_update_delete_movie, get_post_cinema, \
     get_update_delete_cinema, get_post_genre, get_update_delete_genre, \
         get_post_session, get_post_cinemaImage, get_update_delete_session, \
             get_update_delete_cinemaImage, get_post_session, get_post_actor, \
                 get_post_studio, get_update_delete_actor, get_update_delete_studio \
                     getImageByCinema

urlpatterns = [
    path('movies/', get_post_movies),
    path('movies/id/<int:pk>/', get_update_delete_movie),
    path('cinemas/', get_post_cinema),
    path('cinemas/place_id/<str:key>/', get_update_delete_cinema),
    path('genres/', get_post_genre),
    path('genres/id/<int:pk>/', get_update_delete_genre), 
    path('sessions/', get_post_session),
    path('sessions/id/<int:pk>/', get_update_delete_session),
    path('cinema-images/', get_post_cinemaImage),
    path('cinema-images/cinema/<int:pk>/', getImageByCinema),
    path('cinema-images/id/<int:pk>/', get_update_delete_cinemaImage),
    path('actors/', get_post_actor),
    path('actors/id/<int:pk>/', get_update_delete_actor),
    path('studios/', get_post_studio),
    path('studios/id/<int:pk>/', get_update_delete_studio),
]