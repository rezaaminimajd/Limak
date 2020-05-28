from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import (UserSignUpSerializer, EmailSerializer,
                          ResetPasswordConfirmSerializer)


# Create your views here.


class LogoutAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class SignUpAPIView(GenericAPIView):
    serializer_class = UserSignUpSerializer

    def post(self, request):
        from .tasks import send_activation_email

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        send_date = timezone.now() + timezone.timedelta(seconds=5)

        send_activation_email.apply_async(
            [serializer.validated_data['email']],
            eta=send_date
        )

        serializer.save()

        return Response(
            data={'details': _('Activation email sent, check your email')},
            status=status.HTTP_200_OK
        )


class ResendActivationEmailAPIView(GenericAPIView):
    serializer_class = EmailSerializer

    def post(self, request):
        from .tasks import send_activation_email

        data = self.get_serializer(data=request.data).data
        user = get_object_or_404(User, email=data['email'])

        send_date = timezone.now() + timezone.timedelta(seconds=5)
        send_activation_email.apply_async(
            [user.email],
            eta=send_date
        )

        return Response(
            data={'details': _('Activation email sent, check your email')},
            status=status.HTTP_200_OK
        )


class ActivateAccountAPIView(GenericAPIView):

    def get(self, request, eid, token):
        pass


class ResetPasswordAPIView(GenericAPIView):
    serializer_class = EmailSerializer

    def post(self, request):
        from .tasks import reset_password

        data = self.get_serializer(request.data).data
        user = get_object_or_404(User, email=data['email'])

        send_date = timezone.now() + timezone.timedelta(seconds=5)
        reset_password.apply_async(
            [user.id],
            eta=send_date
        )

        return Response(
            data={'details': _('Reset password email sent, check your email')},
            status=status.HTTP_200_OK
        )


class ResetPasswordConfirmAPIView(GenericAPIView):
    serializer_class = ResetPasswordConfirmSerializer

    def post(self, request):
        from .tasks import reset_password_confirm

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        reset_password_confirm.apply_async(
            [data['uid'], data['token'], data['password']]
        )

        return Response(
            data={'details': _('Password changed successfully')},
            status=status.HTTP_200_OK
        )
