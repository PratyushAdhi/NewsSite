from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (ArticleDetailAPIView, ArticleListAPIView, ArticleCreateAPIView)

urlpatterns = [
    path('', ArticleListAPIView.as_view(), name="article-list-create"),
    path('create/', ArticleCreateAPIView.as_view(), name="article-create"),
    path('<slug:slug>/', ArticleDetailAPIView.as_view(), name="article-detail"),
]
