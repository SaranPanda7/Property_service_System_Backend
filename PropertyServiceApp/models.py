from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import ( AbstractUser, )



class User(AbstractUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    username = models.CharField(_('username'),max_length=150,unique=True,)
    fullname = models.CharField(max_length=150, blank=True)
    address = models.TextField(max_length=255, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.email


class Roles(models.Model):
    role = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.role


class Users(models.Model):
    phone_number = models.CharField(max_length=15)
    full_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(max_length=255, blank=True, null=True)
    role = models.ForeignKey(Roles, on_delete=models.DO_NOTHING, null=True, default=1)

    def __str__(self):
        return self.phone_number


