from django.contrib.auth.models import User

from apps.accounts.services.reset_password import ResetPassword
from apps.accounts.services.reset_password_confirm import ResetPasswordConfirm
from apps.accounts.services.send_signup_email import SendSignupEmail
from limak_backend.celery import app


@app.task(name='send_verification_email')
def send_signup_email(user_email: str) -> None:
    send_signup_email_service = SendSignupEmail(user_email)
    send_signup_email_service.send_signup_email()


@app.task(name='reset_password_confirm')
def reset_password_confirm(uid: str, token: str, password: str) -> None:
    reset_password_confirm_service = ResetPasswordConfirm(
        uid, token, password
    )
    reset_password_confirm_service.reset_password_confirm()


@app.task(name='reset_password')
def reset_password(user_id: int) -> None:
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        pass
    else:
        reset_password_service = ResetPassword(user=user)
        reset_password_service.reset_password()
