from django.contrib.auth.hashers import make_password
from django.utils import timezone

from .models import User, Profile, Address


def seed_accounts_app(users=5, addresses=10):
    from django_seed import Seed

    seeder = Seed.seeder()
    seeder.add_entity(User, users, {
        'password': lambda x: make_password('123456')
    })
    # seeder.add_entity(Profile, users)
    seeder.add_entity(Address, addresses)
    pks = seeder.execute()
    for pk in pks[User]:
        Profile.objects.create(user_id=pk, birth_date=timezone.now(),
                               phone_number='0123456789')
