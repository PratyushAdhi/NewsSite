from django.urls import path, include
from .views import (AuthorRetrieveAPIView, AuthorFollowersAPIView, AuthorFollowingAPIView,AuthorFollowAPIView,AuthorArticleAPIView)

urlpatterns = [
    path('<str:username>/', AuthorRetrieveAPIView.as_view(),
         name="author-detail"),
    path('<str:username>/articles/',AuthorArticleAPIView.as_view(), name="author-articles"),
    path('<str:username>/follow/', AuthorFollowAPIView.as_view(), name="author-follow"),
    path('<str:username>/followers/', AuthorFollowersAPIView.as_view(), name="author-followers"),
    path('<str:username>/following/', AuthorFollowingAPIView.as_view(),name="author-following"),
]
