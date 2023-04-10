from django.urls import path
from .views import get_gems, get_gem
urlpatterns = [
    path('gems/', get_gems, name='index'),
    path('gems/<int:gem_id>', get_gem, name='gem'),
]
