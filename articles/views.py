from rest_framework import generics
from .models import Article
from .serializers import ArticleListSerializer


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer