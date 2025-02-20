from django.contrib.sitemaps import Sitemap

from .models import Race


class RaceSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Race.objects.all()



