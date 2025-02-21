from django.contrib.sitemaps import Sitemap
from django.contrib import sitemaps
from django.urls import reverse
from .models import Race, Personage, Gamer, Storyline, Release


class RaceSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Race.objects.all()


class PersonageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Personage.objects.all()


class StorylineSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Storyline.objects.all()

class ReleaseSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Release.objects.all()


class GamerSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Gamer.objects.all()


class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = "monthly"

    def items(self):
        return ['mysite:about']

    def location(self, item):
        return reverse(item)






