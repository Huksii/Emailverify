from django.db import models

from random import randint
from time import sleep

from django.conf import settings
from django.core.mail import send_mail
from django.db import models

class VerifyEmail(models.Model):
    email = models.EmailField()
    code = models.IntegerField(null=True, blank=True)

    def send_message_email(self):
        subject = 'Verify email'
        self.code = randint(100000, 999999)
        self.save()
        message = f'Ваш код подтверждения: {self.code}'
        recipient_list = [self.email]
        email = settings.EMAIL_HOST_USER
        sleep(10)
        send_mail(
            subject=subject,
            message=message,
            recipient_list=recipient_list,
            from_email=email,
            fail_silently=False
        )

    def verify_email(self, code):
        if self.code == code:
            self.send_message_confirm()
            return True
        return False

    def send_message_confirm(self):
        subject = 'Confirm email'
        message = 'Ваш email подтвержден'
        recipient_list = [self.email]
        email = settings.EMAIL_HOST_USER
        send_mail(
            subject=subject,
            message=message,
            recipient_list=recipient_list,
            from_email=email,
            fail_silently=False
        )