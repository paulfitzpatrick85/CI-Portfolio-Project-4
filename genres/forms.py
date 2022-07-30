from .models import Band
from django import forms


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ('band_image', 'band_name', 'band_email', 'band_bio',)

       