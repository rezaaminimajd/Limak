import secrets
from typing import Union

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

__all__ = ('SendSignupEmail',)


class SendSignupEmail:
    def __init__(self, email: str):
        self.email: str = email
        self._eid: str = urlsafe_base64_encode(force_bytes(self.email))

    def send_signup_email(self) -> None:
        self._send_email()
        pass

    def _send_email(self) -> None:
        from django.conf import settings
        from apps.core.utils import send_email

        context = {
            'domain': settings.DOMAIN,
        }

        send_email(
            subject=f'Signup in {"Limak Shop"}',
            template_name='accounts/signup_email.html',
            context=context,
            receipts=[self.email]
        )
