from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

from model_utils.models import UUIDModel, TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class ClotheKind(TimeStampedModel):
    order = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=64, unique=True, primary_key=True)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Clothe(TimeStampedModel, UUIDModel):
    code = models.CharField(max_length=128)
    price = models.IntegerField()
    discounted_price = models.IntegerField(null=True, blank=True)
    is_discounted = models.BooleanField(default=False)
    description = models.CharField(max_length=1024, null=True, blank=True)
    kind = models.ForeignKey('store.ClotheKind', on_delete=models.CASCADE)
    category = models.ForeignKey('store.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class ClotheInfo(TimeStampedModel, UUIDModel):
    clothe = models.ForeignKey('store.Clothe', related_name='information',
                               on_delete=models.CASCADE)
    count = models.IntegerField()
    color = models.ForeignKey('store.ClotheColor', on_delete=models.CASCADE)
    size = models.ForeignKey('store.ClotheSize', on_delete=models.CASCADE)
    for_basket = models.BooleanField(default=False)

    @property
    def is_finish(self):
        return self.count == 0

    def __str__(self):
        return '{} - {}'.format(self.color, self.size)


class ClotheSize(TimeStampedModel):
    order = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=64, unique=True, primary_key=True)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ClotheColor(TimeStampedModel):
    order = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=64, unique=True, primary_key=True)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Basket(UUIDModel, TimeStampedModel):
    user = models.ForeignKey(User, related_name='baskets',
                             on_delete=models.CASCADE)
    payed = models.BooleanField(default=False)

    @property
    def total_price(self):
        return self.products.all().aggregate(total_price=Sum('total_price'))[
            'total_price'
        ]


class ProductInBasket(TimeStampedModel):
    basket = models.ForeignKey('store.Basket',
                               related_name='products',
                               on_delete=models.CASCADE)
    clothe = models.ForeignKey('store.Clothe',
                               related_name='clothes_in_basket',
                               on_delete=models.CASCADE)

    count = models.IntegerField(default=1)

    color = models.ForeignKey('store.ClotheColor',
                              related_name='colors_in_basket',
                              on_delete=models.CASCADE)
    size = models.ForeignKey('store.ClotheSize',
                             related_name='sizes_in_basket',
                             on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total_price = self.count * self.clothe.price
        super().save(*args, **kwargs)
