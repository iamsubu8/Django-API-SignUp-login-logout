
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
import datetime
from .managers import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'
    id=models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    email = models.EmailField(blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    modified_date=models.CharField(max_length=30,blank=True)



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username




