from django.contrib import admin
from .models import Race, Personage, Gamer, Release, Storyline


class RaceAdmin(admin.ModelAdmin):
    model = Race
    list_display = ['id', 'name']
    list_filter = ['name']
    list_display_links = ['id', 'name']


class PersonageAdmin(admin.ModelAdmin):
    model = Personage
    list_display = ['id', 'name','race', 'power', 'dexterity', 'endurance', 'wisdom', 'intellect', 'charisma', 'image']
    # list_filter = []
    list_display_links = ['id', 'name']


class GamerAdmin(admin.ModelAdmin):
    model = Gamer
    list_display = ['id', 'name', 'display_personages', 'image']
    list_filter = ['name']
    list_display_links = ['id', 'name']


class ReleaseAdmin(admin.ModelAdmin):
    model = Release
    list_display = ['id', 'number', 'title', 'display_gamers', 'display_personages','line',  'url',]
    list_display_links = ['id', 'number', 'title']
    list_filter = ['line']


class StorylineAdmin(admin.ModelAdmin):
    model = Storyline
    list_display = ['id', 'line']
    list_display_links = ['id', 'line']


admin.site.register(Race, RaceAdmin)
admin.site.register(Personage, PersonageAdmin)
admin.site.register(Gamer, GamerAdmin)
admin.site.register(Release, ReleaseAdmin)
admin.site.register(Storyline, StorylineAdmin)