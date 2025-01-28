from django.urls import path
from rest_framework import routers
from .views import index,  PersonageListView, ReleaseListView

# from . import views


app_name ='mysite'

# router = routers.DefaultRouter()
# router.register('api/___', ___APIView)


urlpatterns = [
    path('', index, name="index"),
    path("personages/", PersonageListView.as_view(), name="personages"),
    path("releases/", ReleaseListView.as_view(), name="releases"),
]
# urlpatterns += router.urls