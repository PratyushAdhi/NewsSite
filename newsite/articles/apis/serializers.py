from rest_framework import serializers
from ..models import Article
from comments.models import Comments
from authors.apis.serializers import AuthorSerializer

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    voter_count = serializers.SerializerMethodField()
    lookup_field = "slug"

    extra_kwargs = {
        "slug": {
            "read_only": True
        }
    }

    class Meta:
        model = Article
        exclude = ("hidden", "id", "voters",)

    def get_voter_count(self, obj):
        return obj.voters.all().count()   



class ArticleHideSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    comments = serializers.SerializerMethodField()
    voter_count = serializers.SerializerMethodField()
    lookup_field = "slug"

    extra_kwargs = {
        "slug": {
            "read_only": True
        }
    }

    class Meta:
        model = Article
        exclude = ("visibility", "id", "voters",)

    def get_comments(self, obj):
        comments = Comments.objects.filter(article__slug=obj.slug).count()
        return comments

    def get_voter_count(self, obj):
        return obj.voters.all().count()