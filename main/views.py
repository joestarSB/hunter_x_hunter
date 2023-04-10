from django.shortcuts import render
from django.views import generic
from .models import Gems
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'main/index.html', context={
        'title': 'Title'
    })

def get_gems(request):
    gems = Gems.objects.all()
    return render(request, 'main/index.html', context={'gems': gems})


def get_gem(request, gem_id):
    gem = get_object_or_404(Gems, pk=gem_id)
    return render(request, 'main/store.html', context={'gem': gem})
