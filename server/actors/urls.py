from django.urls import path
from . import views

urlpatterns = [
    path('search/actor/<str:query>/', views.searchActor),
    path('', views.actorList),
    path('<int:actor_id>/', views.actorDetail),
]
