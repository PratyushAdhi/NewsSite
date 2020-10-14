from rest_framework import views
from rest_framework.generics import (GenericAPIView,
                                     ListCreateAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView, CreateAPIView)
from django.shortcuts import get_object_or_404
from ..models import Comments
from .serializers import CommentSerializer
from .permissions import IsAuthorOrModeratorOrReadOnly
from articles.models import Article

class CommentListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthorOrModeratorOrReadOnly,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comments.objects.filter(article__slug=self.kwargs['slug'])

    def perform_create(self, serializer, **kwargs):
        author = self.request.user
        slug = self.kwargs['slug']
        article = get_object_or_404(Article, slug=slug)
        serializer.save(article=article, author=author)

class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = "slug"
    permission_classes = (IsAuthorOrModeratorOrReadOnly,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        Comments.objects.filter(article__slug=self.kwargs['slug'], id=self.kwargs["pk"])

