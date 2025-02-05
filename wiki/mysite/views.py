from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.list import ListView


from rest_framework import viewsets
from .serializers import ReleaseSerializer
from .models import Personage, Release, Gamer

# def index(request):
#     return render(request, "index.html")

class PersonageListView(ListView):
    model = Personage
    paginate_by = 15
    allow_empty = False
    template_name = 'personages.html'


class ReleaseListView(ListView):
    model = Release
    paginate_by = 12
    allow_empty = False
    ordering = ['number']
    template_name = 'releases.html'


class GamerListView(ListView):
    model = Gamer
    paginate_by = 15
    template_name = 'gamers.html'


class ReleaseDetailView(DetailView):
    model = Release
    template_name = 'release_detail.html'


class GamerDetailView(DetailView):
    model = Gamer
    template_name = 'gamer_detail.html'


class PersonageDetailView(DetailView):
    model = Personage
    template_name = 'personage_detail.html'




class ReleasAPIView(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
