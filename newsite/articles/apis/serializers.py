from rest_framework import serializers
from ..models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    lookup_field = "slug"

    extra_kwargs = {
        "slug": {
            "read_only": True
        }
    }

    class Meta:
        model = Article
        exclude = ("hidden", "id")


class ArticleHideSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    lookup_field = "slug"

    extra_kwargs = {
        "slug": {
            "read_only": True
        }
    }

    class Meta:
        model = Article
        exclude = ("visibility", "id")
