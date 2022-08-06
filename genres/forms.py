from .models import Genre, Band
from django import forms
from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = 'date'


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ('band_image', 'band_name', 'band_email', 'band_bio', 'next_gig', 'concert_venue')
        widgets = {'next_gig': DateInput(), }
     