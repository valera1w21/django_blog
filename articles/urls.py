from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    CommentListView,
    CommentDeleteView,
)

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/<int:pk>/comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
]