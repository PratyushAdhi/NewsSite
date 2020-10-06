from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (AuthorRetrieveAPIView, RegisterAPIView, 
RefreshToken, PasswordTokenCheckAPIView,VerifyEmail, 
RequestPasswordResetEmailAPIView,LoginAPIView, PasswordResetNewPasswordAPIView)

urlpatterns = [
    path('register/',RegisterAPIView.as_view(), name="regsiter"),
    path('email-verify/', VerifyEmail.as_view(), name="verify-email"),
    path('login/',LoginAPIView.as_view(), name="login"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(), name="password-reset"),
    path('request-reset-email/', RequestPasswordResetEmailAPIView.as_view(), name="request-reset-email"),
    path('password-reset-setup/', PasswordResetNewPasswordAPIView.as_view(),name="password-reset-setup"),
    path('<str:username>/', AuthorRetrieveAPIView.as_view(),
         name="author-detail"),
]
