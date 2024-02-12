# app/management/commands/createsuperuser.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a Django superuser if it does not exist'

    def handle(self, *args, **options):
        print("run createsuperuser.py")
        if not User.objects.filter(username='admin').exists():
            try:
                User.objects.create_superuser(
                    'admin',
                    'admin@example.com',
                    'adminpassword'
                )
                self.stdout.write(self.style.SUCCESS('Successfully created a new superuser'))
            except IntegrityError:
                self.stdout.write(self.style.WARNING('Superuser already exists'))
