from django.contrib import admin
from .models import Genre 
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Genre)
class GenreAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('genre_name',)}  # populate slug(form?) from title
    list_filter = ('status', 'created_on')  # will create filter window/box with status and created today, last 7 days etc
    list_display = ('genre_name', 'slug', 'status', 'created_on')  # titles/info on each post, slug removed
    search_fields = ('genre_name', 'content')  # add search bar in admin page

    summernote_fields = ('content')

