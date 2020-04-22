from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from .serializers import CinemaSerializer, MovieSerializer, SessionSerializer, \
    GenreSerializer, CinemaImageSerializer, ActorSerializer, StudioSerializer
from .models import Cinema, Movie, Session, Genre, CinemaImage, Actor, Studio

#---------------------------------------------------------------------------------
# General
#---------------------------------------------------------------------------------

def general_get_post(request, class_name, serializer_name):
    if request.method == 'GET' :
        obj = class_name.objects.all()
        serializer = serializer_name(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer = serializer_name(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def general_get_put_delete(request, attr, class_name, serializer_name) :
    try:
        obj = class_name.objects.get(pk=attr)
    except class_name.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET' :
        return Response(serializer_name(obj).data)
    elif request.method == 'PUT' :
        serializer = serializer_name(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE' :
        obj.delete()
        return Response(status=status.HTTP_200_OK)

#---------------------------------------------------------------------------------
# Movies
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def getMoviesList(request) :
    return general_get_post(request, Movie, MovieSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getMovieItem(request, pk) :
    return general_get_put_delete(request, pk, Movie, MovieSerializer)

@api_view(['GET'])
def getMoviesByCinema(request, place_id):
    try:
        cinema = Cinema.objects.get(place_id=place_id)
    except Cinema.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    
    sessions = Session.objects.filter(cinema=cinema.pk)
    movies = set([session.movie for session in sessions])
    return Response(MovieSerializer(movies, many=True).data)

@api_view(['GET'])
def getAnnounces(request) :
    announces = Movie.objects.filter(release_date__gt = timezone.localtime(timezone.now())).order_by('release_date')[:15]
    return Response(MovieSerializer(announces, many=True).data)

@api_view(['GET'])
def inRolling(request) :
    movies = Movie.objects.filter(release_date__lt = timezone.localtime(timezone.now())).order_by('release_date')[:15]
    return Response(MovieSerializer(movies, many=True).data)

@api_view(['GET'])
def getMoviesByDate(request, year, day, month) :
    sessions = Session.objects.filter(start_time__date = datetime(year=year, day=day, month=month))
    movies = set([session.movie for session in sessions])
    movies = sorted(movies, key=lambda x: x.rating or 0, reverse=True)
    return Response(MovieSerializer(movies, many=True).data)

@api_view(['GET'])
def getTodayMovies(request) :
    today = timezone.localtime(timezone.now())
    return getMoviesByDate(request._request, today.year, today.day, today.month)

@api_view(['POST'])
def getMovieByName(request) :
    name = request.data['name']
    objs = Movie.objects.all().order_by('-rating')
    result = [obj for obj in objs if name in obj.name]
    return Response(MovieSerializer(result, many=True).data)

#---------------------------------------------------------------------------------
# Cinemas
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def getCinemasList(request) :
    return general_get_post(request, Cinema, CinemaSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getCinemaItem(request, place_id) :
    try:
        obj = Cinema.objects.get(place_id=place_id)
    except Cinema.DoesNotExist:
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET' :
        return Response(CinemaSerializer(obj).data)
    elif request.method == 'PUT' :
        serializer = CinemaSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE' :
        obj.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def getCinemasByMovie(request, pk) :
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    
    sessions = Session.objects.filter(movie=movie.pk)
    cinemas = set([session.cinema for session in sessions])
    return Response(CinemaSerializer(cinemas, many=True).data)
#---------------------------------------------------------------------------------
# Genres
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def getGenresList(request) :
    return general_get_post(request, Genre, GenreSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getGenreItem(request, pk) :
    try:
        obj = Genre.objects.get(pseudo_id=pk)
    except Genre.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET' :
        return Response(GenreSerializer(obj).data)
    elif request.method == 'PUT' :
        serializer = GenreSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE' :
        obj.delete()
        return Response(status=status.HTTP_200_OK)


#---------------------------------------------------------------------------------
# Sessions
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def getSessionsList(request) :
    return general_get_post(request, Session, SessionSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getSessionItem(request, pk) :
    return general_get_put_delete(request, pk, Session, SessionSerializer)

@api_view(['GET'])
def getSessionsByMovie(request, pk) :
    objs = Session.objects.filter(movie=pk)
    return Response(SessionSerializer(objs, many=True).data) 

@api_view(['GET'])
def getSessionsByCinema(request, place_id) :
    try:
        cinema = Cinema.objects.get(place_id=place_id)
    except Cinema.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    objs = Session.objects.filter(cinema=cinema.pk)
    return Response(SessionSerializer(objs, many=True).data) 


#---------------------------------------------------------------------------------
# Cinema Images
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def getCinemaImagesList(request) :
    return general_get_post(request, CinemaImage, CinemaImageSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getCinemaImageItem(request, pk) :
    return general_get_put_delete(request, pk, CinemaImage, CinemaImageSerializer)

@api_view(['GET'])
def getImagesByCinema(request, place_id) :
    try:
        cinema = Cinema.objects.get(place_id=place_id)
    except Cinema.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    objs = CinemaImage.objects.filter(cinema=cinema.pk)
    return Response(CinemaImageSerializer(objs, many=True).data) 


#---------------------------------------------------------------------------------
# Actors
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def getActorsList(request) :
    return general_get_post(request, Actor, ActorSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getActorItem(request, pk) :
    return general_get_put_delete(request, pk, Actor, ActorSerializer)


#---------------------------------------------------------------------------------
# Studios
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def getStudiosList(request) :
    return general_get_post(request, Studio, StudioSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getStudioItem(request, pk) :
    return general_get_put_delete(request, pk, Studio, StudioSerializer)
