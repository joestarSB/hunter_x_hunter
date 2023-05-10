from django.shortcuts import render

def account(request):
    return render(request, 'authapp/account.html', context={
        'title': 'Title'
    })
