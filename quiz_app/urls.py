from django.urls import path
from .import views

urlspattern = [
    path('', views.index, name='index'),
    path('', views.landing, name='landing'),
]