from . import views
from django.urls import path


urlpatterns = [
    path('', views.GenreList.as_view(), name='home'),
    path('<slug:slug>/', views.GenreDetail.as_view(), name='genre_detail'),
]