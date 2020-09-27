from rest_framework import serializers
from ..models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    lookup_field = "slug"

    class Meta:
        model = Article
        fields = "__all__"
