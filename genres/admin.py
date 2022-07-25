from django.contrib import admin
from .models import Genre, Genre_lite, Band
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Genre)
class GenreAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('genre_name',)}  # populate slug(form?) from title
    search_fields = ('genre_name', 'content')  # add search bar in admin page
    summernote_fields = ('content')


@admin.register(Genre_lite)
class Genre_lite_Admin(SummernoteModelAdmin):
    prepopulated_fields = {'slug_lite': ('genre_lite_name',)}  # populate slug(form?) from title
    search_fields = ('genre_lite_name', 'content')  # add search bar in admin page
    summernote_fields = ('content')


@admin.register(Band)
class BandAdmin(SummernoteModelAdmin):
    search_fields = ('band_name', 'band_email', 'bio_body')
    actions = ['approve_comments']    

    def approve_bands(self, request, queryset):
        queryset.update(approved=True)    


