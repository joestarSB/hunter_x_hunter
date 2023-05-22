from django.shortcuts import render, redirect
from django.views import generic
from .models import Gems
from django.shortcuts import get_object_or_404
from .forms import BuyGemForm


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


def buy_gem(request, gem_id):
    gem = get_object_or_404(Gems, pk=gem_id)
    gem.users = request.user
    form = BuyGemForm(request.POST or None)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            gem.users.add(request.user)
            return redirect('index')
    return render(request, template_name='main/buy_gem.html', context={
        'form': form,
        'title': 'Покупка гемов',
        'error': error
    })
