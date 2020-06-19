from django.db import models


class Information(models.Model):
    address = models.CharField(max_length=1024)
    telephone_number = models.CharField(max_length=64)
    instagram_id = models.CharField(max_length=256)
    telegram_id = models.CharField(max_length=256)
    twitter_id = models.CharField(max_length=256)

    def __str__(self):
        return 'Information'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        query = Information.objects.all()
        if len(query) == 0:
            super(Information, self).save()
