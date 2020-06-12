from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.store.models import Basket
from .models import ReadyToLoadOrder


@receiver(pre_save, sender=ReadyToLoadOrder)
def update_basket(sender, instance: ReadyToLoadOrder, created, **kwargs):
    if instance.id is not None:
        if instance.loaded:
            instance.order.sent = True
            instance.order.save()
