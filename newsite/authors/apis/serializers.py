from rest_framework import serializers
from ..models import Author


class AuthorSerializer(serializers.ModelSerializer):
    lookup_field = "username"
    follower_count = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ("username", "name", "email", "bio", "date_joined", "display_picture","follower_count",)

    def get_follower_count(self, obj):
        return obj.followers.count()


class AuthorMinSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ("username", "display_picture",)

