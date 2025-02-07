from django.views.generic import DetailView
from django.views.generic.list import ListView


from rest_framework import viewsets
from .serializers import ReleaseSerializer, RaceSerializer, PersonageSerializer, GamerSerializer, StorylineSerializer
from .models import Personage, Release, Gamer, Race, Storyline


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gamer_id = self.kwargs.get('pk')
        context["releases"] = Release.objects.filter(gamers__pk=gamer_id).order_by('number')
        return context


class PersonageDetailView(DetailView):
    model = Personage
    template_name = 'personage_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        personage_id = self.kwargs.get('pk')
        context["releases"] = Release.objects.filter(personages__pk=personage_id).order_by('number')
        return context


class PersonageListFilterView(ListView):
    model = Personage
    paginate_by = 15
    allow_empty = False
    template_name = 'personages_filter.html'

    def get_queryset(self):
        race_id = self.kwargs.get('pk')
        return Personage.objects.filter(race=race_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        race_id = self.kwargs.get('pk')
        context["race"] = Race.objects.get(pk=race_id).name
        return context


class ReleaseListFilterView(ListView):
    model = Release
    paginate_by = 15
    allow_empty = False
    template_name = 'releases_filter.html'

    def get_queryset(self):
        line_id = self.kwargs.get('pk')
        return Release.objects.filter(line=line_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        line_id = self.kwargs.get('pk')
        context["line"] = Storyline.objects.get(pk=line_id).line
        return context












# API
class ReleasAPIView(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class RacesAPIView(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class PersonagesAPIView(viewsets.ModelViewSet):
    queryset = Personage.objects.all()
    serializer_class = PersonageSerializer


class GamersAPIView(viewsets.ModelViewSet):
    queryset = Gamer.objects.all()
    serializer_class = GamerSerializer


class StorylinesAPIView(viewsets.ModelViewSet):
    queryset = Storyline.objects.all()
    serializer_class = StorylineSerializer


