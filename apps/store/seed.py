from random import choice
from django.contrib.auth.hashers import make_password
from django.utils import timezone

from .models import (Category, Clothe, ClotheInfo, ClotheSize, ClotheKind,
                     ClotheColor)


def seed_accounts_app():
    from django_seed import Seed

    seeder = Seed.seeder()
    seeder.add_entity(Category, 10)
    seeder.add_entity(ClotheKind, 10)
    seeder.add_entity(Clothe, 20)

    for i, name in enumerate(['s', 'm', 'l', 'xl', 'xll', 'xlll']):
        ClotheSize.objects.create(order=i, name=name)

    for i, name in enumerate(
            ['red', 'blue', 'brown', 'blak', 'white', 'grey']):
        ClotheColor.objects.create(order=i, name=name)

    seeder.add_entity(ClotheInfo, 60)

    pks = seeder.execute()
