from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Genre
from .forms import BandForm


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
                "band_added": False,
                "band_form": BandForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):    
        queryset = Genre.objects.filter(status=1)   
        genre = get_object_or_404(queryset, slug=slug)  
        bands = genre.bands.filter(band_approved=True)
        band_form = BandForm(data=request.POST)

        if band_form.is_valid():
            band_form.instance.email = request.user.email
            band_form.instance.name = request.user.username
            band = band_form.save(commit=False)
            band.genre = genre
            band.save()
        else:
            band_form = BandForm() 


        return render(
            request,            
            "genre_detail.html",       
            {
                "genre": genre,          
                "bands": bands,
                "band_added": True,
                "band_form": BandForm(),
            },
        )
