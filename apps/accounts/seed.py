from .models import User, Profile, Address


def seed_accounts_app(users=5, addresses=10):
    from django_seed import Seed
    seeder = Seed.seeder()
    seeder.add_entity(User, users)
    seeder.add_entity(Profile, users)
    seeder.add_entity(Address, addresses)


