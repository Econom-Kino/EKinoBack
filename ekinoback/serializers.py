from rest_framework import serializers
from ekinoback.models import Cinema, Movie, Session, Genre, CinemaImage, \
    Studio, Actor

class GenreSerializer(serializers.ModelSerializer) :

    class Meta:
        model = Genre
        fields = '__all__'

class StudioSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Studio
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Actor
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer) :

    class Meta:
        model = Cinema
        fields = '__all__'
    

class MovieSerializer(serializers.ModelSerializer) :
    genre_names = GenreSerializer(many=True, source='genre', read_only=True)
    actors_names = ActorSerializer(many=True, source='actors', read_only=True)
    studio_names = StudioSerializer(many=True, source='studio', read_only=True)
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all() , many=True, write_only=True, slug_field='name')
    actors = serializers.SlugRelatedField(queryset=Actor.objects.all() , many=True, write_only=True, slug_field='name')
    studio = serializers.SlugRelatedField(queryset=Studio.objects.all() , many=True, write_only=True, slug_field='name')

    class Meta:
        model = Movie
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer) :
    # cinema_name = CinemaSerializer(read_only=True, source='cinema')
    # movie_name = MovieSerializer(read_only=True, source='movie')
    cinema = serializers.SlugRelatedField(queryset = Cinema.objects.all(), slug_field = 'name')
    movie = serializers.SlugRelatedField(write_only = True, queryset = Movie.objects.all(), slug_field = 'name')

    class Meta:
        model = Session
        fields = '__all__'
        depth = 1

class CinemaImageSerializer(serializers.ModelSerializer) :

    class Meta:
        model = CinemaImage
        fields = '__all__'