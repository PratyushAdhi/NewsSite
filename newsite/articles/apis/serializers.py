from rest_framework import serializers
from ..models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    lookup_field = "slug"

    class Meta:
        model = Article
        fields = "__all__"


class ArticleHideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("body", "visibility", "author")
        extra_kwargs = {
            "body": {
                "read_only": True
            },
            "author": {
                "read_only": True
            }
        }
