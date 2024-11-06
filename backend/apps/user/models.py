from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
import uuid


class CustomUser(AbstractUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    USERNAME_FIELD = 'username'
