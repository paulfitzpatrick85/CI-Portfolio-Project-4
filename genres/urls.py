from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.GenreList.as_view(), name='home'),
    path('<slug:slug>/', views.GenreDetail.as_view(), name='genre_detail'),
    path('edit_band.html/<band_id>/', views.edit_band, name='edit_band'),
    path('delete_band.html/<band_id>/', views.delete_band, name='delete_band'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)