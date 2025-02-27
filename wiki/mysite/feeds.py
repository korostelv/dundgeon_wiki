from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse
from .models import Release, Personage


class LatestReleaseFeed(Feed):
    title = "ПЧК - последние выпуски"
    link = "/feeds/"
    description = "Новые выпуски."

    def items(self):
        return Release.objects.order_by('-number')[:5]

    def item_number(self, item):
        return item.number

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.created_at



