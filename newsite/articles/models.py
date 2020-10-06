from django.db import models
from django.conf import settings
from django.utils.text import slugify
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
    #claps = models.ManyToManyField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    visibility = models.CharField(
        max_length=15, choices=VISIBILITY, default="public")
    hidden = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            slug = self.author.username + "-" + self.title
            self.slug = slugify(slug)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
