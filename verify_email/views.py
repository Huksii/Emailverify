from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import VerifyEmail
from .serializers import VerifyEmailSerializer, VerifyEmailConfirm


class VerifyEmailView(viewsets.ModelViewSet):
    queryset = VerifyEmail.objects.all()
    serializer_class = VerifyEmailSerializer
    http_method_names = ['post']

class VerifyEmailConfirmView(viewsets.ModelViewSet):
    queryset = VerifyEmail.objects.all()
    serializer_class = VerifyEmailConfirm
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        code = request.data.get('code')

        instance = VerifyEmail.objects.filter(email=email).first()

        if instance is not None:
            if instance.verify_email(int(code)):
                return Response({'message': 'Почта подтверждена!'}, status=status.HTTP_200_OK)
            return Response({'message': 'Неверный код!'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': f'Пользователь с почтой {email} не найден'},
                        status=status.HTTP_400_BAD_REQUEST)