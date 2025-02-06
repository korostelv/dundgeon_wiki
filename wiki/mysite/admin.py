from django.contrib import admin
from .models import Race, Personage, Gamer, Release, Storyline
from django.utils.html import format_html


class RaceAdmin(admin.ModelAdmin):
    model = Race
    list_display = ['id', 'name']
    list_filter = ['name']
    list_display_links = ['id', 'name']


class PersonageAdmin(admin.ModelAdmin):
    model = Personage
    list_display = ['id', 'name', 'race', 'power', 'dexterity', 'endurance', 'wisdom', 'intellect', 'charisma', 'gamer',
                    'display_image']
    list_filter = ['race', 'gamer']
    list_display_links = ['id', 'name']

    def display_image(self, obj):
        return format_html('<img src="{}" width="35" height="50" />', obj.image.url)

    display_image.short_description = 'Изображение персонажа'


class GamerAdmin(admin.ModelAdmin):
    model = Gamer
    list_display = ['id', 'name', 'display_personages', 'display_image']
    list_filter = ['name']
    list_display_links = ['name']

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)

    display_image.short_description = 'Фото игрока'


class ReleaseAdmin(admin.ModelAdmin):
    model = Release
    list_display = ['id', 'number', 'title','annotation', 'display_gamers', 'display_personages', 'line', 'url', 'display_image']
    list_display_links = ['id', 'number', 'title']
    list_filter = ['line']

    def display_image(self, obj):
        return format_html('<img src="{}" width="100" height="50" />', obj.image.url)

    display_image.short_description = 'Обложки выпуска'


class StorylineAdmin(admin.ModelAdmin):
    model = Storyline
    list_display = ['id', 'line']
    list_display_links = ['id', 'line']


admin.site.register(Race, RaceAdmin)
admin.site.register(Personage, PersonageAdmin)
admin.site.register(Gamer, GamerAdmin)
admin.site.register(Release, ReleaseAdmin)
admin.site.register(Storyline, StorylineAdmin)
