from django.db import models
from django.conf import settings
from articles.models import Article
# Create your models here.
class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField()
    media = models.FileField(upload_to="comments/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {
            "author": self.author,
            "body": self.body
        }

