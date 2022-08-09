from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Genre, Band
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
        

        if request.method == 'POST':                          
            band_form = BandForm(request.POST, request.FILES)          
        if band_form.is_valid():
            band_form.instance.band_email = request.user.email
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


def edit_band(request, band_id):
    band_form = BandForm(data=request.GET)
    band = get_object_or_404(Band, id=band_id)
    if request.method == 'POST':                          
        band_form = BandForm(request.POST, request.FILES, instance=band)   # populate with existing data       
        if band_form.is_valid():
            # band_form.instance.band_email = request.user.email
            # band_form.instance.name = request.user.username
            # band = band_form.save(commit=False)
            #band.genre = genre
            band.save()
            return redirect('genre_detail.html')
    
    #band_form = BandForm(instance=band)
    context = {"band_form": BandForm}
    return render(request, 'edit_band.html', context)
    
        