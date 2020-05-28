from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)


class Clothe(models.Model):
    code = models.CharField(max_length=128)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    is_discounted = models.BooleanField(default=False)
    description = models.CharField(max_length=1024)
    kind = models.ForeignKey('store.ClotheKind', on_delete=models.CASCADE)


class ClotheInfo(models.Model):
    clothe = models.ForeignKey('store.Clothe', related_name='information',
                               on_delete=models.CASCADE)
    count = models.IntegerField()
    color = models.OneToOneField('store.ClotheColor', on_delete=models.CASCADE)
    size = models.OneToOneField('store.ClotheSize', on_delete=models.CASCADE)

    @property
    def is_finish(self):
        return self.count == 0


class ClotheSize(models.Model):
    order = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=64)
    enable = models.BooleanField(default=True)


class ClotheKind(models.Model):
    order = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=64)
    enable = models.BooleanField(default=True)


class ClotheColor(models.Model):
    order = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=64)
    enable = models.BooleanField(default=True)
