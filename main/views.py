from django.shortcuts import render
from django.views import generic
from .models import Gems


def index(request):
    return render(request, 'main/index.html', context={
        'title': 'Title'
    })

def get_gems(request):
    gems = Gems.objects.all()
    return render(request, 'main/index.html', context={'gems': gems})
