from django.shortcuts import render
from django.views import generic
from .models import Genre


class GenreList(generic.ListView):
    model = Genre
    queryset = Genre.objects.filter(status=1).order_by('-created_on')  # change back to 'word' to order alphabetically
    template_name = 'index.html'     # html file that view will render
    paginate_by = 4        # limit number of post to 6, if there are more django will add page navagation
