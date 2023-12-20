from rest_framework import serializers
from .models import VerifyEmail

class VerifyEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyEmail
        fields = ['email']

    def create(self, validated_data):
        instance, created = VerifyEmail.objects.update_or_create(
            email=validated_data['email']
        )
        instance.send_message_email()
        return instance


class VerifyEmailConfirm(serializers.ModelSerializer):
    class Meta:
        model = VerifyEmail
        fields = ['email', 'code']
