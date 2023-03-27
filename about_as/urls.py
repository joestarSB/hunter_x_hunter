from django.urls import path
from .views import index

urlpatterns = [
    path('about_as/', index, name='about'),
]
