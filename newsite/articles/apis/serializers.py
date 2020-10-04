from rest_framework import serializers
from ..models import Article
from comments.models import Comments
from authors.apis.serializers import AuthorSerializer

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
    author = AuthorSerializer()
    comments = serializers.SerializerMethodField()
    lookup_field = "slug"

    extra_kwargs = {
        "slug": {
            "read_only": True
        }
    }

    class Meta:
        model = Article
        exclude = ("visibility", "id")

    def get_comments(self, obj):
        comments = Comments.objects.filter(article__slug=obj.slug).count()
        return comments
