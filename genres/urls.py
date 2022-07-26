from . import views
from django.urls import path


urlpatterns = [
    path('', views.GenreList.as_view(), name='home'),
    path('', views.Genre_liteList.as_view(), name='home'),   
]