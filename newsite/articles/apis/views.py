from rest_framework import views
from rest_framework.generics import (GenericAPIView,
                                     ListCreateAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     CreateAPIView)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import Article
from .serializers import ArticleSerializer, ArticleHideSerializer
from .permissions import IsAuthorOrModeratorOrReadOnly



class ArticleListAPIView(ListAPIView):
    permission_classes = (IsAuthorOrModeratorOrReadOnly,IsAuthenticatedOrReadOnly)
    queryset = Article.objects.filter(
        visibility="public", hidden=False).order_by("-updated_at")
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(visibility="public", hidden=False)
    lookup_field = "slug"
    permission_classes = (IsAuthorOrModeratorOrReadOnly,IsAuthenticatedOrReadOnly)

    def get_serializer_class(self):
        if self.request.user.is_moderator or self.request.is_admin:
            return ArticleHideSerializer
        return ArticleSerializer

class ArticleCreateAPIView(CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthorOrModeratorOrReadOnly, IsAuthenticatedOrReadOnly)
    def get_queryset(self):
        return Article.objects.all()

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)