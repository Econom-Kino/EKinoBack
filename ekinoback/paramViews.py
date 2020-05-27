from django.http import HttpResponse
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from .serializers import *
from .models import *

#---------------------------------------------------------------------------------
# Utilities
#---------------------------------------------------------------------------------
def getNow() :
    return timezone.localtime(timezone.now())

#---------------------------------------------------------------------------------
# Movies
#---------------------------------------------------------------------------------
@api_view(['GET'])
def getMoviesByCinema(request, place_id):
    """
    Get Movies by Cinema

    URL for getting of Movies, Sessions of which are in specific Cinema
    """
    try:
        cinema = Cinema.objects.get(place_id=place_id)
    except Cinema.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    
    sessions = Session.objects.filter(cinema=cinema.pk)
    movies = set([session.movie for session in sessions])
    return Response(MovieSerializer(movies[:16], many=True).data)

@api_view(['GET'])
def getAnnounces(request) :
    """
    Get not released Movies

    URL for getting of Movies, that are still not released
    """
    announces = Movie.objects.filter(release_date__gt = getNow()).order_by('release_date')[:15]
    return Response(MovieSerializer(announces, many=True).data)

@api_view(['GET'])
def inRolling(request) :
    """
    Get released Movies

    URL for getting of Movies, that are released
    """
    movies = Movie.objects.filter(release_date__lt = getNow()).order_by('release_date')[:16]
    return Response(MovieSerializer(movies, many=True).data)

@api_view(['GET'])
def getMoviesByDate(request, year, day, month) :
    """
    Get Movies by date

    URL for getting of Movies, Sessions of which has start date same as specified
    """
    sessions = Session.objects.filter(start_time__date = datetime(year=year, day=day, month=month))
    movies = set([session.movie for session in sessions])
    movies = sorted(movies, key=lambda x: x.rating or 0, reverse=True)
    return Response(MovieSerializer(movies[:16], many=True).data)

@api_view(['GET'])
def getTodayMovies(request) :
    """
    Get Movies by today

    Redirects to GetMoviesByDate with today parameters
    """
    today = getNow()
    return getMoviesByDate(request._request, today.year, today.day, today.month)

@api_view(['POST'])
def getMovieByName(request) :
    """
    Get Movies by name

    URL for getting of Movies, that have specified string in its 'name' field
    """
    objs = Movie.objects.filter(name__icontains=request.data['name']).order_by('-rating')
    return Response(MovieSerializer(objs, many=True).data)

#---------------------------------------------------------------------------------
# Cinemas
#---------------------------------------------------------------------------------
@api_view(['GET'])
def getCinemasByMovie(request, pk) :
    """
    Get Cinemas by Movie

    URL for getting of Cinemas, that have sessions of specified Movie
    """
    sessions = Session.objects.filter(movie=pk)
    cinemas = set([session.cinema for session in sessions])
    return Response(CinemaSerializer(cinemas, many=True).data)

#---------------------------------------------------------------------------------
# Sessions
#---------------------------------------------------------------------------------
@api_view(['GET'])
def getSessionsByMovie(request, pk) :
    """
    Get Sessions by Movie

    URL for getting of Sessions of specified Movie
    """
    objs = Session.objects.filter(movie=pk, start_time__gt=getNow()).order_by('price')[:30]
    return Response(SessionSerializer(objs, many=True).data) 

@api_view(['GET'])
def getSessionsByCinema(request, place_id) :
    """
    Get Sessions by Cinema

    URL for getting of Sessions at specified Cinema
    """
    try:
        cinema = Cinema.objects.get(place_id=place_id)
    except Cinema.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    objs = Session.objects.filter(cinema=cinema.pk, start_time__gt=getNow())[:30]
    return Response(SessionSerializer(objs, many=True).data) 

@api_view(['GET'])
def getSessionsByMovieAndDate(request, pk, year, day, month) :
    """
    Get Sessions by Movie and Date

    URL for getting of Sessions of specified Movie and at specified Date at the same time
    """
    if (day in range(1,32) and month in range(1,13)) :
        objs = Session.objects.filter(movie=pk, start_time__date=datetime(year=year, day=day, month=month))\
            .filter(start_time__gt=getNow()).order_by('price')
        return Response(SessionSerializer(objs, many=True).data)
    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getSessionsByBoth(request, place_id, pk) :
    """
    Get Sessions by Movie and Cinema

    URL for getting of Sessions of specified Movie and at specified Cinema at the same time
    """
    try:
        cinema = Cinema.objects.get(place_id=place_id)
    except Cinema.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    sessions = Session.objects.filter(cinema=cinema.id, movie=pk, start_time__gt=getNow())[:30]
    return Response(SessionSerializer(sessions, many=True).data)

#---------------------------------------------------------------------------------
# Cinema Images
#---------------------------------------------------------------------------------
@api_view(['GET'])
def getImagesByCinema(request, place_id) :
    """
    Get Images of Cinema

    URL for getting of CinemaImages of specified Cinema
    """
    try:
        cinema = Cinema.objects.get(place_id=place_id)
    except Cinema.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    objs = CinemaImage.objects.filter(cinema=cinema.pk)
    return Response(CinemaImageSerializer(objs, many=True).data) 

#---------------------------------------------------------------------------------
# Special
#---------------------------------------------------------------------------------
@api_view(['GET'])
def clearUselessSessions(request) :
    """
    Delete Useless Sessions

    URL for deletion of sessions, that are older than now !!!FOR ADMIN USE ONLY!!!
    """
    Session.objects.filter(start_time__lt=getNow()).delete()
    return HttpResponse(status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def clearUselessMovies(request) :
    """
    Delete Useless Movies

    URL for deletion of movies, that are already released and have no sessions !!!FOR ADMIN USE ONLY!!!
    """
    sessions = Session.objects.all()
    useful = list(set([session.movie for session in sessions]))
    Movie.objects.all(release_date__lt = getNow()).exclude(id__in=[movie.id for movie in useful]).delete()
    return HttpResponse(status.HTTP_202_ACCEPTED)
