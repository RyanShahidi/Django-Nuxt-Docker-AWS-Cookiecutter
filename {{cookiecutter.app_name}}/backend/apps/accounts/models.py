import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    objects = CustomUserManager()
    email = models.EmailField(unique=True)
