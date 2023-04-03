from django.urls import path
from .views import index, get_gems

urlpatterns = [
    path('', get_gems, name='index')
]
