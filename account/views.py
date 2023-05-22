from django.shortcuts import render
from .models import UID

def account(request):
    return render(request, 'authapp/account.html', context={
        'title': 'Title'
    })

def UID_view(request):
    pass