from django.shortcuts import render
from django.views import generic
from .models import Genre


class GenreList(generic.ListView):
    model = Genre
    template_name = 'index.html'   
    paginate_by = 6
