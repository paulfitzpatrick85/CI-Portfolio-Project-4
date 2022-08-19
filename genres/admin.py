from django.contrib import admin
from .models import Genre, Band
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Genre)
class GenreAdmin(SummernoteModelAdmin):
    # populate slug(form?) from title
    prepopulated_fields = {'slug': ('genre_name',)}
    search_fields = ('genre_name', 'content')
    summernote_fields = ('content')
    actions = ['approve_genre']
    # titles/info on each post
    list_display = ('genre_name', 'approved', 'slug', 'status')


@admin.register(Band)
class BandAdmin(SummernoteModelAdmin):
    search_fields = ('band_name', 'band_email', 'bio_body')
    actions = ['approve_band']
    list_display = ('band_name', 'band_approved', 'status')

    def approve_bands(self, request, queryset):
        queryset.update(approved=True)
