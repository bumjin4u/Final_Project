from django.urls import path
from . import views
urlpatterns = [
    path("", views.tagList),
    path('<int:tag_id>/', views.tagDetail),
]
