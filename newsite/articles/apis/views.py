from rest_framework.views import APIView
from rest_framework.generics import (GenericAPIView,
                                     ListCreateAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     CreateAPIView)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from ..models import Article
from .serializers import ArticleSerializer, ArticleHideSerializer
from .permissions import IsAuthorOrModeratorOrReadOnly, IsNotAuthorAndAuthenticated
from authors.models import Author


class ArticleListAPIView(ListAPIView):
    permission_classes = [IsAuthorOrModeratorOrReadOnly,IsAuthenticatedOrReadOnly]
    queryset = Article.objects.filter(
        visibility="public", hidden=False).order_by("-updated_at")
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(visibility="public", hidden=False)
    lookup_field = "slug"
    permission_classes = [IsAuthorOrModeratorOrReadOnly,IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_moderator or self.request.user.is_staff:
                return ArticleHideSerializer
        return ArticleSerializer

class ArticleCreateAPIView(CreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthorOrModeratorOrReadOnly,IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        return Article.objects.all()

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)

class ArticleLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an answer instance."""
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsNotAuthorAndAuthenticated]

    def delete(self, request, slug):
        """Remove request.user from the voters queryset of an answer instance."""
        article = Article.objects.get(slug=slug)
        user = request.user

        article.voters.remove(user)
        article.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(article, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug):
        """Add request.user to the voters queryset of an answer instance."""
        article = Article.objects.get(slug=slug)
        user = request.user

        article.voters.add(user)
        article.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(article, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

class AuthorFollowArticleAPIView(ListAPIView):
    serializer_class = ArticleSerializer
    
    def get_queryset(self):
        curr = self.request.user
        user = Author.objects.get(username=curr.username)
        sum = 0
        following_list = user.following.all()
        sum = Article.objects.filter(author__username=following_list[0].username)
        for user in range(1, len(following_list)):
            another = Article.objects.filter(author__username=following_list[user].username)
            sum = sum.union(another, all=True)

        return sum.order_by("-created_at")

class PrivateArticleAPIView(ListAPIView):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(author__username=self.request.user.username, visibility=False)
