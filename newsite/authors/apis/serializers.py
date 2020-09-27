from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Author


class AuthorSerializer(serializers.ModelSerializer):
    lookup_field = "username"

    class Meta:
        model = Author
        fields = ("username", "name", "email", "bio", "date_joined")
