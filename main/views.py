from django.shortcuts import render
from django.views import generic
from .models import Gems


def index(request):
    return render(request, 'main/index.html', context={
        'title': 'Title'
    })

class GemsDetailView(generic.DetailView):
    model = Gems
