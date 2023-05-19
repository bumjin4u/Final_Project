from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list), # articles 조회, 생성
    path('<int:article_pk>/', views.article_detail), # article 조회, 수정, 삭제
    path('<int:article_pk>/comments/', views.comment_list), # comments 조회, 생성
    path('comments/<int:comment_id>/', views.comment_update), # comment 수정, 삭제
]