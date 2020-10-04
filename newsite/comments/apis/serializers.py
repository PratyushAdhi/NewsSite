from rest_framework import serializers
from ..models import Comments
from articles.apis.serializers import ArticleSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    article = serializers.StringRelatedField()
    class Meta:
        fields = "__all__"
        model = Comments