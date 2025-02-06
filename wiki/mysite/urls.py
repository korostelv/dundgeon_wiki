from django.urls import path
from rest_framework import routers
from .views import (PersonageListView, ReleaseListView, ReleaseDetailView, GamerListView,
                    GamerDetailView, PersonageDetailView, PersonageListFilterView, ReleaseListFilterView,
                    ReleasAPIView, RacesAPIView, PersonagesAPIView, GamersAPIView, StorylinesAPIView)

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
    path('releases_filter/<int:pk>/', ReleaseListFilterView.as_view(), name='releases_filter'),
]
urlpatterns += router.urls
