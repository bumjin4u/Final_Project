from django.urls import path
from . import views

urlpatterns = [
    path('search/actor/<str:query>/', views.searchActor),
]
