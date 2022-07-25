from django.shortcuts import render
from django.views import generic
from .models import Genre, Genre_lite


class GenreList(generic.ListView):
    model = Genre
    template_name = 'index.html'   
    

class Genre_lite_List(generic.ListView):
    model = Genre_lite
    template_name = 'index.html'   
