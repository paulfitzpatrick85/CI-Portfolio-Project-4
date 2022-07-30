from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Genre


class GenreList(generic.ListView):
    model = Genre
    template_name = 'index.html'   
    paginate_by = 6


class GenreDetail(View):

    def get(self, request, slug, *args, **kwargs):    
        queryset = Genre.objects.filter(status=1)   
        genre = get_object_or_404(queryset, slug=slug)  
        bands = genre.bands.filter(band_approved=True)

        return render(
            request,            
            "genre_detail.html",       
            {
                "genre": genre,          # render dictionary
                "bands": bands,
            },
        )