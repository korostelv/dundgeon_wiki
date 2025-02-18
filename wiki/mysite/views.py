from platform import release

from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.db.models import Q
from django.shortcuts import render


from rest_framework import viewsets
from .serializers import ReleaseSerializer, RaceSerializer, PersonageSerializer, GamerSerializer, StorylineSerializer
from .models import Personage, Release, Gamer, Race, Storyline, Picture
from .permissions import IsAdminOrReadOnly


class PersonageListView(ListView):
    model = Personage
    paginate_by = 15
    allow_empty = False
    ordering = ['pk']
    template_name = 'personages.html'


class ReleaseListView(ListView):
    model = Release
    paginate_by = 12
    allow_empty = False
    ordering = ['number','title']
    template_name = 'releases.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["storyline"] = Storyline.objects.all()
        return context


class ReleaseStoryListView(ListView):
    model = Release
    paginate_by = 12
    ordering = ['number', 'title']
    template_name = 'releases_filter.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Release.objects.filter(line__pk=query)
        return Release.objects.all()

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        # context["storyline"] = Storyline.objects.all()
        context['line'] = Storyline.objects.get(pk=query).line
        return context


class GamerListView(ListView):
    model = Gamer
    paginate_by = 15
    ordering = ['pk']
    template_name = 'gamers.html'


class ReleaseDetailView(DetailView):
    model = Release
    template_name = 'release_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        release_id = self.kwargs.get('pk')
        context["pictures"] = Picture.objects.filter(release__pk=release_id)
        return context


class GamerDetailView(DetailView):
    model = Gamer
    template_name = 'gamer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gamer_id = self.kwargs.get('pk')
        context["releases"] = Release.objects.filter(gamers__pk=gamer_id).order_by('number')
        context["personages"] = Personage.objects.filter(gamer__pk=gamer_id)

        return context


class PersonageDetailView(DetailView):
    model = Personage
    template_name = 'personage_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        personage_id = self.kwargs.get('pk')
        context["releases"] = Release.objects.filter(personages__pk=personage_id).order_by('number')
        context["pictures"] = Picture.objects.filter(personage__pk=personage_id)
        return context


class PersonageListFilterView(ListView):
    model = Personage
    paginate_by = 15
    allow_empty = False
    ordering = ['pk']
    template_name = 'personages_filter.html'

    def get_queryset(self):
        race_id = self.kwargs.get('pk')
        return Personage.objects.filter(race=race_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        race_id = self.kwargs.get('pk')
        context["race"] = Race.objects.get(pk=race_id).name
        return context


class PersonageListSearchView(ListView):
    model = Personage
    paginate_by = 15
    ordering = ['pk']
    template_name = 'personages.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Personage.objects.filter(Q(name__icontains=query))
        return Personage.objects.all()


class GamerListSearchView(ListView):
    model = Gamer
    paginate_by = 15
    ordering = ['pk']
    template_name = 'gamers.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Gamer.objects.filter(Q(name__icontains=query))
        return Gamer.objects.all()


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
    permission_classes = (IsAdminOrReadOnly,)


class RacesAPIView(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    permission_classes = (IsAdminOrReadOnly,)


class PersonagesAPIView(viewsets.ModelViewSet):
    queryset = Personage.objects.all()
    serializer_class = PersonageSerializer
    permission_classes = (IsAdminOrReadOnly,)


class GamersAPIView(viewsets.ModelViewSet):
    queryset = Gamer.objects.all()
    serializer_class = GamerSerializer
    permission_classes = (IsAdminOrReadOnly,)


class StorylinesAPIView(viewsets.ModelViewSet):
    queryset = Storyline.objects.all()
    serializer_class = StorylineSerializer
    permission_classes = (IsAdminOrReadOnly,)


#page 404
def page_not_found(request, exception):
    return render(request, 'mysite/404.html', {'path': request.path}, status=404)

#about
def about(request):
    return render(request, 'about.html')





