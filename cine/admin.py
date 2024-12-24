from django.contrib import admin
from cine.models import Cine, Genre, streaming, Actor, Director, Producer


class CineAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'streaming', 'debut_year', 'actor', 'director', 'producers', 'original_writer', 'resume', 'photo')
    search_fields = ('title', 'resume')
    

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class streamingAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Cine, CineAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(streaming, streamingAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Producer, ProducerAdmin)

