from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class AppUserManager(BaseUserManager):
    def create_user(self, email, city, password=None): 
        if not email: 
            raise ValueError("An email is required.") 
        if not city: 
            raise ValueError("A city is required.") 
        email = self.normalize_email(email) 
        user = self.model(email=email, city=city) 
        user.set_password(password) 
        user.save() 
        return user

    def create_superuser(self, email, username, password=None):
        if not username:
            raise ValueError("An username is required.")
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class AppUser(AbstractUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = AppUserManager()

    def __str__(self):
        return self.username
