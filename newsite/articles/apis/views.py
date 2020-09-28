from rest_framework import views
from rest_framework.generics import (GenericAPIView,
                                     ListCreateAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView)

from ..models import Article
from .serializers import ArticleSerializer, ArticleHideSerializer
from .permissions import IsAuthorOrModeratorOrReadOnly


class ArticleListAPIView(ListAPIView):
    permission_classes = (IsAuthorOrModeratorOrReadOnly)
    queryset = Article.objects.filter(
        visibility="public").order_by("-updated_at")
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(visibility="public")
    lookup_field = "slug"
    permission_classes = (IsAuthorOrModeratorOrReadOnly)

    def get_serializer_class(self):
        if self.request.user.is_moderator or self.request.is_admin:
            return ArticleHideSerializer
        return ArticleSerializer
