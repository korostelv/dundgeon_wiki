from django.urls import path
from django.views.generic import TemplateView
from rest_framework import routers
from .views import (PersonageListView, ReleaseListView, ReleaseDetailView, GamerListView,
                    GamerDetailView, PersonageDetailView, PersonageListFilterView,
                    PersonageListSearchView, GamerListSearchView, ReleaseStoryListView, ReleaseListFilterView,
                    ReleasAPIView, RacesAPIView, PersonagesAPIView, GamersAPIView, StorylinesAPIView, about, map)

from .feeds import LatestReleaseFeed

from django.contrib.sitemaps.views import sitemap
from .sitemaps import RaceSitemap, PersonageSitemap, GamerSitemap, StorylineSitemap, ReleaseSitemap, StaticViewSitemap

sitemaps = {
    'race': RaceSitemap,
    'personage': PersonageSitemap,
    'gamer': GamerSitemap,
    'storyline': StorylineSitemap,
    'release': ReleaseSitemap,
    "static": StaticViewSitemap,
}

app_name = 'mysite'

router = routers.DefaultRouter()
router.register('api/releases', ReleasAPIView)
router.register('api/races', RacesAPIView)
router.register('api/personages', PersonagesAPIView)
router.register('api/gamers', GamersAPIView)
router.register('api/storylines', StorylinesAPIView)


urlpatterns = [
    path("personages/", PersonageListView.as_view(), name="personages"),
    path("", ReleaseListView.as_view(), name="releases"),
    path("gamers/", GamerListView.as_view(), name="gamers"),
    path('releases/<int:pk>/', ReleaseDetailView.as_view(), name='release_detail'),
    path('gamers/<int:pk>/', GamerDetailView.as_view(), name='gamer_detail'),
    path('personages/<int:pk>/', PersonageDetailView.as_view(), name='personage_detail'),
    path('personages_filter/<int:pk>/', PersonageListFilterView.as_view(), name='personages_filter'),
    path('personages/search', PersonageListSearchView.as_view(), name='personages_search'),
    path('gamers/search', GamerListSearchView.as_view(), name='gamers_search'),
    path('releases_filter/<int:pk>/', ReleaseListFilterView.as_view(), name='releases_filter'),
    path('releases_filter/', ReleaseStoryListView.as_view(), name='releases_story'),
    path('about', about, name='about'),
    path('map', map, name='map'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots"),
    path('feeds', LatestReleaseFeed(), name='feeds'),
]
urlpatterns += router.urls

handler404 = 'mysite.views.page_not_found'
