from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (ArticleDetailAPIView, ArticleListAPIView, ArticleCreateAPIView, ArticleLikeAPIView, AuthorFollowArticleAPIView, PrivateArticleAPIView)

urlpatterns = [
    path('', ArticleListAPIView.as_view(), name="article-list-create"),
    path('create/', ArticleCreateAPIView.as_view(), name="article-create"),
    path('following/', AuthorFollowArticleAPIView.as_view(), name="author-follow"),
    path('private/', PrivateArticleAPIView.as_view(), name="article-private-view"),
    path('<slug:slug>/', ArticleDetailAPIView.as_view(), name="article-detail"),
    path('<slug:slug>/like/', ArticleLikeAPIView.as_view(),name="article-like"),
]
