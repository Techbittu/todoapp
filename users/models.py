from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Użytkownik musi posiadać adres email!")
        if not password:
            raise ValueError("Użytkownik musi posiadać hasło!")
        if not username:
            raise ValueError("Użytkownik musi podać nazwę konta!")
        user_obj = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            is_staff=True
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff=True
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    email               = models.EmailField(max_length=80, unique=True)
    username            = models.CharField(max_length=30, unique=True)
    data_joined         = models.DateTimeField(verbose_name="data joined", auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_admin            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    