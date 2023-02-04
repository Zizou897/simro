from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50, blank=True, null=True)