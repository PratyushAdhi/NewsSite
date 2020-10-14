from django.core.mail import EmailMessage
from django.conf import settings
class Utils:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data["email_subject"], body=data["email_body"], to=[data["to_email"]])
        email.send()
        # send_mail(data["email_subject"],data["email_body"], settings.EMAIL_HOST_USER, [data["to_email"]], fail_silently=False)