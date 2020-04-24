from django.http import HttpResponse
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from .serializers import *
from .models import *

#---------------------------------------------------------------------------------
# General
#---------------------------------------------------------------------------------

def general_get_post(request, class_name, serializer_name):
    if request.method == 'GET' :
        obj = class_name.objects.all()
        serializer = serializer_name(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        serializer = serializer_name(data=request.data, many=False)
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
    """
    Get/Post MovieList

    URL for getting/posting of Movies list
    """
    return general_get_post(request, Movie, MovieSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getMovieItem(request, pk) :
    """
    Get/Put/Delete Movie instance

    URL for getting/putting/deleting of Movie instance
    """
    return general_get_put_delete(request, pk, Movie, MovieSerializer)

#---------------------------------------------------------------------------------
# Cinemas
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def getCinemasList(request) :
    """
    Get/Post CinemaList

    URL for getting/posting of Cinemas list
    """
    return general_get_post(request, Cinema, CinemaSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getCinemaItem(request, place_id) :
    """
    Get/Put/Delete Cinema instance

    URL for getting/putting/deleting of Cinema instance
    """
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

#---------------------------------------------------------------------------------
# Genres
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def getGenresList(request) :
    """
    Get/Post GenreList

    URL for getting/posting of Genres list
    """
    return general_get_post(request, Genre, GenreSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getGenreItem(request, pk) :
    """
    Get/Put/Delete Genre instance

    URL for getting/putting/deleting of Genre instance
    """
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
    """
    Get/Post SessionList

    URL for getting/posting of Sessions list
    """
    return general_get_post(request, Session, SessionSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getSessionItem(request, pk) :
    """
    Get/Put/Delete Session instance

    URL for getting/putting/deleting of Session instance
    """
    return general_get_put_delete(request, pk, Session, SessionSerializer)

#---------------------------------------------------------------------------------
# Cinema Images
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def getCinemaImagesList(request) :
    """
    Get/Post CinemaImageList

    URL for getting/posting of Cinema Images list
    """
    return general_get_post(request, CinemaImage, CinemaImageSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getCinemaImageItem(request, pk) :
    """
    Get/Put/Delete CinemaImage instance

    URL for getting/putting/deleting of CinemaImage instance
    """
    return general_get_put_delete(request, pk, CinemaImage, CinemaImageSerializer)

#---------------------------------------------------------------------------------
# Actors
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def getActorsList(request) :
    """
    Get/Post ActorList

    URL for getting/posting of Actors list
    """
    return general_get_post(request, Actor, ActorSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getActorItem(request, pk) :
    """
    Get/Put/Delete Actor instance

    URL for getting/putting/deleting of Actor instance
    """
    return general_get_put_delete(request, pk, Actor, ActorSerializer)


#---------------------------------------------------------------------------------
# Studios
#---------------------------------------------------------------------------------
@api_view(['GET', 'POST'])
def getStudiosList(request) :
    """
    Get/Post StudioList

    URL for getting/posting of Studios list
    """
    return general_get_post(request, Studio, StudioSerializer)

@api_view(['GET', 'PUT', 'DELETE'])
def getStudioItem(request, pk) :
    """
    Get/Put/Delete Studio instance

    URL for getting/putting/deleting of Studio instance
    """
    return general_get_put_delete(request, pk, Studio, StudioSerializer)
