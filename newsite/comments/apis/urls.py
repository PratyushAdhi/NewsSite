from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import CommentDetailAPIView, CommentListCreateAPIView

urlpatterns = [
    path('<slug:slug>/', CommentListCreateAPIView.as_view(), name="comment-list-create"),
    path('<slug:slug>/<int:pk>/', CommentDetailAPIView.as_view(), name="comment-detail"),
]
