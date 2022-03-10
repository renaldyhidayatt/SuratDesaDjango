from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
from apps.utils.models import Timestamp

# Create your models here.
class Users(AbstractBaseUser, Timestamp, PermissionsMixin):
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=13)
    image = models.ImageField(default="profile/undraw_profile.svg")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["name"]

    objects = UserManager()

    def __str__(self):
        return self.email