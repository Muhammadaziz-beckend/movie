from django.contrib import admin
from .models import *


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title','release_date','reting','cauntry')
    list_display_links = ('id','title','release_date','reting','cauntry')
    list_filter = ('cauntry','release_date','reting','age','genre')
    search_fields = ('id','title','reting','cauntry','age')

    readonly_fields = ('reting',)


@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    list_display = ('id','movie',)
    list_display_links = ('id','movie',)
    list_filter = ('movie',)
    search_fields = ('movie',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_links = ('id','name',)
    search_fields = ('name',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','movie','user','like','dislike','catigori_review')
    list_display_links = ('id','movie','user','like','dislike','catigori_review')
    list_filter = ('movie','user','catigori_review')
    search_fields = ('movie','user')

@admin.register(Catigori_review)
class Catigori_reviewAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_links = ('id','name',)
    search_fields = ('name',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id','name','date_fo_birth','heght','total_movis','birthplace','active_years')
    list_display_links = ('id','name','date_fo_birth','heght','total_movis','birthplace','active_years')
    list_filter = ('birthplace','career', 'movies','genres')
    search_fields = ('name','heght','birthplace','movies','active_years')

    readonly_fields = ('total_movis',)


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_links = ('id','name',)
    search_fields = ('name',)


@admin.register(Photos_actor)
class Photos_actorAdmin(admin.ModelAdmin):
    list_display = ('id','actor',)
    list_display_links = ('id','actor',)
    list_filter = ('actor',)


@admin.register(Cauntry)
class CauntryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_links = ('id','name',)
    search_fields = ('name',)