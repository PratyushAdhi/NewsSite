from rest_framework.generics import RetrieveAPIView, GenericAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Author
from .serializers import AuthorSerializer, AuthorMinSerializer
from articles.apis.serializers import ArticleSerializer
from articles.models import Article


class AuthorRetrieveAPIView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = "username"

class AuthorFollowersAPIView(ListAPIView):
    serializer_class = AuthorMinSerializer
    lookup_field = "username"

    def get_queryset(self, **kwargs):
        username = self.kwargs["username"]
        print("followers")
        return Author.objects.get(username=username).followers.all()


class AuthorFollowingAPIView(ListAPIView):
    serializer_class = AuthorMinSerializer
    lookup_field = "username"

    def get_queryset(self, **kwargs):
        username = self.kwargs["username"]
        user = Author.objects.get(username=username).following.all()
        return user

class AuthorFollowAPIView(APIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = "username"

    def delete(self, request, username):
        """Remove request.user from the voters queryset of an answer instance."""
        author = Author.objects.get(username=username)
        user = request.user

        author.followers.remove(user)
        author.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(author, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, username):
        """Add request.user to the voters queryset of an answer instance."""
        author = Author.objects.get(username=username)
        user = request.user

        author.followers.add(user)
        author.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(author, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

        
class AuthorArticleAPIView(ListAPIView):

    serializer_class = ArticleSerializer

    def get_queryset(self, **kwargs):
        username = self.kwargs["username"]
        return Article.objects.filter(author__username=username).order_by("-created_at")