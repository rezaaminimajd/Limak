from random import choice
from django.contrib.auth.hashers import make_password
from django.utils import timezone

from .models import (Category, Clothe, ClotheInfo, ClotheSize, ClotheKind,
                     ClotheColor)


def seed_store_app():
    from django_seed import Seed

    seeder = Seed.seeder()
    seeder.add_entity(Category, 10)
    seeder.add_entity(ClotheKind, 10, {
        'name': lambda x: seeder.faker.name()
    })
    seeder.add_entity(Clothe, 20)

    try:
        for i, name in enumerate(['s', 'm', 'l', 'xl', 'xll', 'xlll']):
            ClotheSize.objects.create(order=i, name=name)
    except Exception:
        pass
    try:
        for i, name in enumerate(
                ['red', 'blue', 'brown', 'black', 'white', 'grey']):
            ClotheColor.objects.create(order=i, name=name)
    except Exception:
        pass
    seeder.add_entity(ClotheInfo, 60, {
        'color': lambda x: choice(list(ClotheColor.objects.all())),
        'size': lambda x: choice(list(ClotheSize.objects.all()))
    })

    pks = seeder.execute()
