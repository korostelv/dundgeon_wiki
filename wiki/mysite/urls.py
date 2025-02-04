from django.urls import path
from rest_framework import routers
from .views import  PersonageListView, ReleaseListView, ReleaseDetailView, GamerListView, GamerDetailView,PersonageDetailView, ReleasAPIView




app_name ='mysite'

router = routers.DefaultRouter()
router.register('api/releases', ReleasAPIView)


urlpatterns = [
    # path('', index, name="index"),
    path("personages/", PersonageListView.as_view(), name="personages"),
    path("", ReleaseListView.as_view(), name="releases"),
    path("gamers/", GamerListView.as_view(), name="gamers"),
    path('releases/<int:pk>/', ReleaseDetailView.as_view(), name='release_detail'),
    path('gamers/<int:pk>/', GamerDetailView.as_view(), name='gamer_detail'),
    path('personages/<int:pk>/', PersonageDetailView.as_view(), name='personage_detail'),
]
urlpatterns += router.urls