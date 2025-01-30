from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.list import ListView


from rest_framework import viewsets
# from .serializers import
from .models import Personage, Release

def index(request):
    return render(request, "index.html")

class PersonageListView(ListView):
    model = Personage
    paginate_by = 10
    allow_empty = False
    template_name = 'personages.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class ReleaseListView(ListView):
    model = Release
    paginate_by = 10
    allow_empty = False
    template_name = 'releases.html'


class ReleaseDetailView(DetailView):
    model = Release
    context_object_name = 'release'
    template_name = 'release_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# class ___APIView(viewsets.ModelViewSet):
#     queryset = ___.objects.all()
#     serializer_class = ___Serializer
