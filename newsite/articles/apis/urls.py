from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (ArticleDetailAPIView, ArticleListAPIView)

urlpatterns = [
    path('', ArticleListAPIView.as_view(), name="article-list-create"),
    path('<str:slug>/', ArticleDetailAPIView.as_view(), name="article-detail")
]
