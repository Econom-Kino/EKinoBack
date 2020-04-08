from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
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
def get_post_movies(request) :
    return general_get_post(request, Movie, MovieSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete_movie(request, pk) :
    return general_get_put_delete(request, pk, Movie, MovieSerializer)

#---------------------------------------------------------------------------------
# Cinemas
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def get_post_cinema(request) :
    return general_get_post(request, Cinema, CinemaSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete_cinema(request, key) :
    try:
        obj = Cinema.objects.get(place_id=key)
    except Cinema.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

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

#---------------------------------------------------------------------------------
# Genres
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def get_post_genre(request) :
    return general_get_post(request, Genre, GenreSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete_genre(request, pk) :
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
def get_post_session(request) :
    return general_get_post(request, Session, SessionSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete_session(request, pk) :
    return general_get_put_delete(request, pk, Session, SessionSerializer)

@api_view(['GET'])
def getSessionByMovie(request, pk) :
    obj = Session.objects.filter(movie=pk)
    return Response(CinemaImageSerializer(obj, many=True).data) 

@api_view(['GET'])
def getSessionByCinema(request, pk) :
    obj = CinemaImage.objects.filter(cinema=pk)
    return Response(CinemaImageSerializer(obj, many=True).data) 

#---------------------------------------------------------------------------------
# Cinema Images
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def get_post_cinemaImage(request) :
    return general_get_post(request, CinemaImage, CinemaImageSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete_cinemaImage(request, pk) :
    return general_get_put_delete(request, pk, CinemaImage, CinemaImageSerializer)

@api_view(['GET'])
def getImageByCinema(request, place_id) :
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
def get_post_actor(request) :
    return general_get_post(request, Actor, ActorSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete_actor(request, pk) :
    return general_get_put_delete(request, pk, Actor, ActorSerializer)

#---------------------------------------------------------------------------------
# Studios
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def get_post_studio(request) :
    return general_get_post(request, Studio, StudioSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete_studio(request, pk) :
    return general_get_put_delete(request, pk, Studio, StudioSerializer)

