from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields import EmailField
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.


class AuthorManager(BaseUserManager):

    def create_user(self, email, username, password):
        email = self.normalize_email(email)
        if not email:
            raise ValidationError("Email not provided")
        if not username:
            raise ValidationError("No username")
        author = self.model(
            email=email,
            username=username
        )
        author.set_password(password)
        author.save(using=self._db)
        return author

    def create_superuser(self, email, username, password):
        author = self.create_user(
            email=email,
            username=username,
            password=password
        )
        author.is_admin = True
        author.is_staff = True
        author.is_superuser = True
        author.is_moderator = True
        author.is_verified = True
        author.save(using=self._db)
        return author


class Author(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    followers = models.ManyToManyField("self", related_name="following", symmetrical=False)
    display_picture = models.ImageField(
        null=True, blank=True, upload_to="authors/")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password", "username"]

    objects = AuthorManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

