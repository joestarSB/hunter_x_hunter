from django.urls import path
from .views import index, get_gems
urlpatterns = [
    path('', get_gems, name='index'),
    path('gems/<int:gem_id>', get_gems, name='gems'),
]
