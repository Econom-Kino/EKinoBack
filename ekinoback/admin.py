from django.contrib import admin
from .models import Movie, Session, Genre, Cinema, Actor, Studio, CinemaImage


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'duration', 'country_production', 'director', 'rating')
    list_display_links = ('name',)
    search_fields = ('name',)


class SessionAdmin(admin.ModelAdmin):
    list_display = ('cinema', 'movie', 'price', 'start_time', 'language', 'technology')
    list_display_links = ('cinema', 'movie')
    search_fields = ('cinema__name', 'movie__name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'pseudo_id',)
    list_display_links = ('name', 'pseudo_id',)
    search_fields = ('name',)
    
    
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'longitude', 'latitude', 'website_link', 'phone',)
    list_display_links = ('name',)
    search_fields = ('name',)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class StudioAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

class CinemaImageAdmin(admin.ModelAdmin):
    list_display = ('image_link',)
    list_display_links = ('image_link',)
    search_fields = ('image_link',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Studio, StudioAdmin)
admin.site.register(CinemaImage, CinemaImageAdmin)