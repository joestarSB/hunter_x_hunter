from django.shortcuts import render


def index(request):
    return render(request, 'about_as/about.html', context={
        'title': 'Title'
    })

