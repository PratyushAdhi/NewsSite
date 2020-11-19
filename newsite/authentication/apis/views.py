from rest_framework.generics import RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
import jwt
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import reverse
from authors.models import Author
from .serializers import RegisterSerializer, LoginSerializer, RequestPasswordResetEmailSerializer, SetNewPasswordSerializer
from .utils import Utils


class RegisterAPIView(GenericAPIView):

    queryset = Author.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data 
        serializer = RegisterSerializer(data = user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        user = Author.objects.get(email=user_data["email"])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        # relative_link = reverse('verify-email')
        # absurl = "http://" + current_site + relative_link + "?token="+str(token)
        # email_body = absurl
        # data = {
            # "email_body": email_body,
            # "email_subject": "Verify Email",
            # "to_email": user.email
        # }
        # Utils.send_email(data)


        return Response(data=user_data, status=status.HTTP_201_CREATED)

class VerifyEmail(GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = Author.objects.get(id=payload["user_id"])
            if not user.is_verified:
                user.is_verified=True
                user.save()
            return Response({
                    "email": "Successfully activated"
                }, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({
                "message": "Link Expired"
            }, status=status.HTTP_400_BAD_REQUEST)


        
class LoginAPIView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class RequestPasswordResetEmailAPIView(GenericAPIView):
    serializer_class = RequestPasswordResetEmailSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')

        if Author.objects.filter(email=email).exists():
            user = Author.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relative_link = reverse(
                'password-reset', kwargs={'uidb64': uidb64, 'token': token})
            absurl = "http://" + current_site + relative_link
            email_body = absurl
            data = {
            "email_body": email_body,
            "email_subject": "Verify Email",
            "to_email": user.email
            }
            Utils.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPIView(GenericAPIView):

    def get(self, request, uidb64, token):
        try:
            id = smart_bytes(urlsafe_base64_decode(uidb64))
            user = Author.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response(
                    {"error": "Try again"},status=status.HTTP_401_UNAUTHORIZED
                )

            return Response({
                "success":True,
                "message": "Validation Complete",
                "uidb64": uidb64,
                "token": token
            }, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError:
            return Response({
                "error": "Token invalid"
            },status=status.HTTP_401_UNAUTHORIZED)

class PasswordResetNewPasswordAPIView(GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        user = request.data
        serializer = SetNewPasswordSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        return Response({
            "message": "password reset"},
            status=status.HTTP_200_OK
        )


