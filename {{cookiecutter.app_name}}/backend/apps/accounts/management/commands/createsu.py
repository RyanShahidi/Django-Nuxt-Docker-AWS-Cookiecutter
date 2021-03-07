from django.core.management.base import BaseCommand
from apps.accounts.models import CustomUser
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not CustomUser.objects.filter(username=os.environ.get("SUPERUSER_USERNAME")).exists():
            CustomUser.objects.create_superuser(os.environ.get("SUPERUSER_USERNAME"), os.environ.get("SUPERUSER_EMAIL"), os.environ.get("SUPERUSER_PASSWORD"))