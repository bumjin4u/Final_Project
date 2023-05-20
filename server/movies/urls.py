from django.urls import path
from . import views

urlpatterns = [
    path('search/movie/<str:query>/', views.searchMovie),
    path('', views.movieList),
    path('<int:movie_id>/', views.movieDetail),
]
