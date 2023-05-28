from django.urls import path
from .views import get_gems, buy_gem, get_gem
urlpatterns = [
    path('', get_gems, name='index'),
    path('gems/<int:gem_id>', get_gem, name='gem'),
    path('gems/buy/<int:gem_id>', buy_gem, name='buy_gem'),
]
