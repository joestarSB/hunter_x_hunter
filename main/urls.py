from django.urls import path
from .views import index, get_gems, gems_view

urlpatterns = [
    path('', get_gems, name='index'),
    path('gems/<int:gem_id>', gems_view, name='godnota'),
]
