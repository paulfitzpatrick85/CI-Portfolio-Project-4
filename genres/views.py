from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Genre, Band
from .forms import BandForm
from django.contrib.auth.models import User


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


def user_bands(request):
    logged_in_user = request.user
    logged_in_user_bands = Band.objects.filter(author=logged_in_user)
    return render(request, 'genre_detail.html', {'band': logged_in_user_bands})


def edit_band(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    # Authenticated user views and edits only their own bands
    if band.band_email != request.user.email: 
        return redirect('/')
    else:
        band_form = BandForm(data=request.GET)
        
        if request.method == 'POST':                          
            band_form = BandForm(request.POST, request.FILES, instance=band)   # populate with existing data    
            if band_form.is_valid():
                band_form.instance.band_email = request.user.email
                band_form.instance.band_name = request.user.username
                band.save()
                return redirect('/')
            else:
                # Prepopulation happens here:
                data = {"band_name": band.band_name,
                        "band_image": band.band_image, 
                        "band_email": band.band_email, 
                        "band_bio": band.band_bio,
                        "next_gig": band.next_gig,
                        "concert_venue": band.concert_venue, }  
                band_form = BandForm(initial=data) 
                
        context = {"band_form": BandForm(instance=band)}
        return render(request, 'edit_band.html', context)


def delete_band(request, band_id):
    
    band = get_object_or_404(Band, id=band_id)
    # Authenticated usercan delete only their own bands
    if band.band_email != request.user.email: 
        return redirect('/')
    else:
        band.delete()
    return redirect('/')