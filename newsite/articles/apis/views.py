from rest_framework import views
from rest_framework.generics import (GenericAPIView,
                                     ListCreateAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView)

from ..models import Article
from .serializers import ArticleSerializer


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all().order_by("-updated_at")
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "slug"
