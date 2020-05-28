import secrets
from typing import Union

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from gamein_backend.celery import app

from ..models import ActivateUserToken

__all__ = ('SendActivationEmail',)


class SendActivationEmail:
    def __init__(self, email: str):
        self.email: str = email
        self._eid: str = urlsafe_base64_encode(force_bytes(self.email))

        self._activation_token: Union[None, ActivateUserToken] = None

    def send_activation_email(self) -> None:
        self._create_activation_token()
        self._send_email()
        pass

    def _create_activation_token(self) -> None:
        ActivateUserToken.objects.filter(eid=self._eid).filter(
            valid=True).update(valid=False)

        self._activation_token = ActivateUserToken.objects.create(
            token=secrets.token_urlsafe(32),
            eid=self._eid,
        )

    def _send_email(self) -> None:
        from django.conf import settings
        from apps.core.utils import send_email

        context = {
            'domain': settings.DOMAIN,
            'eid': self._activation_token.eid,
            'token': self._activation_token.token,
        }

        send_email(
            subject=f'Account activation in {"Gamein Challenge"}',
            template_name='accounts/activation_email.html',
            context=context,
            receipts=[self.email]
        )
