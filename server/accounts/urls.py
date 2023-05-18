from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_pk>/follow/', views.follow),
    path('<str:username>/profile/', views.profile),
]