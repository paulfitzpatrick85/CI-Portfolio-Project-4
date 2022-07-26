from django.contrib import admin
from .models import Genre, Genre_lite, Band
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Genre)
class GenreAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('genre_name',)}  # populate slug(form?) from title
    search_fields = ('genre_name', 'content')  # add search bar in admin page
    summernote_fields = ('content')
    actions = ['approve_genre']
    list_display = ('genre_name', 'approved', 'slug', 'status')  # titles/info on each post


@admin.register(Genre_lite)
class Genre_liteAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug_lite': ('genre_lite_name',)}  # populate slug(form?) from title
    search_fields = ('genre_lite_name', 'content')  # add search bar in admin page
    summernote_fields = ('content')
    actions = ['approve_genre']
    list_display = ('genre_lite_name', 'approved', 'slug_lite', 'status_lite')


@admin.register(Band)
class BandAdmin(SummernoteModelAdmin):
    search_fields = ('band_name', 'band_email', 'bio_body')
    actions = ['approve_band']    

    def approve_bands(self, request, queryset):
        queryset.update(approved=True)    


# def approve_selected(modeladmin, request, queryset):
#     rows_updated = queryset.approve(active=0)
#     for obj in queryset: obj.save()
#     if rows_updated == 1:
#         message_bit = '1 item was'
#     else:
#         message_bit = '%s items were' % rows_updated
#     modeladmin.message_user(request, '%s successfully approve.' % message_bit)
#     approve_selected.short_description = "approve selected items"

# # add deactivates 
# admin.site.add_action(approve_selected)