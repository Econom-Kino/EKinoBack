from django.db import models
from django.core.validators import RegexValidator

class Genre(models.Model) :
    name = models.CharField(max_length=20, db_index=True, verbose_name='Назва жанру', unique=True)
    pseudo_id = models.IntegerField(verbose_name='номер жанру', db_index=True, default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Жанри'
        verbose_name = 'Жанр'
        ordering = ['name']

class Actor(models.Model) :
    name = models.CharField(max_length=50, verbose_name="Ім'я")

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name_plural = 'Актори'
        verbose_name = 'Актор'
        ordering = ['name']

class Studio(models.Model) :
    name = models.CharField(max_length=50, verbose_name='назва')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Студії'
        verbose_name = 'Студія'
        ordering = ['name']

class Movie(models.Model) :
    name = models.CharField(max_length=200, db_index=True, verbose_name='Назва', unique=True)  
    trailer_link = models.URLField(verbose_name='Посилання на трейлер',)
    poster_link = models.URLField(verbose_name='Посилання на постер',)
    genre = models.ManyToManyField(Genre, verbose_name='Жанр',)
    age = models.BooleanField(verbose_name='Вікове обмеження',)
    rating = models.FloatField(db_index=True, verbose_name='Рейтинг',)
    imdb_id = models.CharField(max_length=63, verbose_name='Номер в базі imdb', default='null')
    duration = models.IntegerField(verbose_name='Тривалість',)
    release_date = models.DateField(verbose_name="Дата прем'єри")
    actors = models.ManyToManyField(Actor, verbose_name='Актори', blank=True)
    country_production = models.CharField(max_length=200, verbose_name='Країна',)
    director = models.CharField(max_length=200, verbose_name='Режисер',)
    studio = models.ManyToManyField(Studio, verbose_name='Студія', blank=True)
    description = models.TextField(verbose_name='Опис',)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Фільми'
        verbose_name = 'Фільм'
        ordering = ['name']

class Cinema(models.Model) :
    name = models.CharField(max_length=100, db_index=True, verbose_name='Назва', unique=True)
    address = models.CharField(max_length=100, verbose_name='Адреса',)
    rating = models.FloatField(verbose_name='Рейтинг кінотеатру',)
    place_id = models.CharField(verbose_name='Код кінотеатру в Google API', max_length=255,)
    longitude = models.FloatField(verbose_name='Довгота',)
    latitude = models.FloatField(verbose_name='Широта',)
    website_link = models.URLField(verbose_name='посилання на сайт')
    phone = models.CharField( max_length=17, blank=True, verbose_name='Мобільний номер')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Кінотеатри'
        verbose_name = 'Кінотеатр'
        ordering = ['name']

class Session(models.Model) :
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='Кінотеатр', null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фільм', null=True)
    price = models.IntegerField(db_index=True, verbose_name='Ціна (грн.)',)
    start_time = models.DateTimeField(verbose_name='Час і дата початку',)
    ticket_link = models.URLField(verbose_name='Посилання на квиток',)
    language = models.CharField(db_index=True, max_length=20, verbose_name='Мова озвучування',)
    technology = models.CharField(db_index=True, max_length=20, verbose_name='Технологія',)

    def __str__(self):
        return self.movie.name
    
    class Meta:
        verbose_name_plural = 'Сеанси'
        verbose_name = 'Сеанс'
        ordering = ['price']

class CinemaImage(models.Model) :
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='кінотеатр', null=True, blank=True)
    image_link = models.URLField(verbose_name='Посилання на фото')

    def __str__(self) :
        return self.cinema.name

    class Meta:
        verbose_name_plural='Галерея'
        verbose_name = 'Фото'
        ordering = ['cinema']
