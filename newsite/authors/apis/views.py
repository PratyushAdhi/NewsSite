from rest_framework.generics import RetrieveAPIView
from ..models import Author
from .serializers import AuthorSerializer


class AuthorRetrieveAPIView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = "username"
