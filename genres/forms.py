from .models import Band
from django import forms
# from django.forms import ModelForm


# class DateInput(forms.DateInput):
#     input_type = 'date'


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ('band_image', 'band_name', 'band_email', 'band_bio', 'concert_venue')
        #widgets = {'upcoming_tour_dates': DateInput(), }
     