from django.db import models
from django.conf import settings
from .utils import unique_slug_generator

# Create your models here.


class Article(models.Model):

    VISIBILITY = (
        ("private", "Private"),
        ("public", "Public")
    )

    media = models.FileField(upload_to="articles/", blank=True, null=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="votes")
    visibility = models.CharField(
        max_length=15, choices=VISIBILITY, default="public")
    hidden = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            slug = unique_slug_generator(self)
            self.slug = slug
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

