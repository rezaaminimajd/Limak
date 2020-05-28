from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',
                                on_delete=models.CASCADE)

    birth_date = models.DateField()
    phone_number = models.CharField(max_length=32)


class Address(models.Model):
    user = models.ForeignKey(User, related_name='addresses',
                             on_delete=models.CASCADE)

    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)

    postal_code = models.IntegerField()
    postal_address = models.TextField()
    house_number = models.IntegerField()
    unit = models.PositiveSmallIntegerField(blank=True, null=True)


class ResetPasswordToken(models.Model):
    EXPIRATION_TIME = 24 * 60 * 60

    uid = models.CharField(max_length=128)
    token = models.CharField(max_length=128)
    expiration_date = models.DateField()

    expired = models.BooleanField(default=False)

    def make_expired(self):
        self.expired = True
        self.save()


class ActivateUserToken(models.Model):
    token = models.CharField(max_length=128)
    eid = models.CharField(max_length=128, null=True)

    valid = models.BooleanField(default=True)
