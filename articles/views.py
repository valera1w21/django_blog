from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .models import Article, Comment
from .permissions import IsAdminOrReadOnly, IsAdminUserOnly
from .serializers import (
    ArticleListSerializer,
    ArticleDetailSerializer,
    ArticleWriteSerializer,
    CommentSerializer,
)

class ArticleListView(generics.ListCreateAPIView):
  

    queryset = Article.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ArticleWriteSerializer
        return ArticleListSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
   

    queryset = Article.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return ArticleWriteSerializer
        return ArticleDetailSerializer
    
class CommentListView(generics.ListCreateAPIView):

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(article_id=self.kwargs['pk'])

    def perform_create(self, serializer):
        article = get_object_or_404(Article, pk=self.kwargs['pk'])
        serializer.save(author=self.request.user, article=article)


class CommentDeleteView(generics.DestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUserOnly]