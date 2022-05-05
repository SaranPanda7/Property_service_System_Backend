from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractUser, )
from django.contrib.postgres.fields import JSONField


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True,)
    username = models.CharField(_('username'), max_length=150, unique=True,)
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
    role = models.ForeignKey(
        Roles, on_delete=models.DO_NOTHING, null=True, default=1)

    def __str__(self):
        return self.full_name


class PropertyTracing(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=0, related_name='property_tracing')
    property_title = models.CharField(max_length=255, blank=True, null=True)
    property_type = models.CharField(max_length=55, blank=True, null=True)
    property_description = models.CharField(
        max_length=255, blank=True, null=True)
    available_days = models.JSONField(blank=True, null=True)
    available_time = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.property_title


# {
# "user" : "6",
# "property_title" : "ABC",
# "property_type" : "house",
# "property_description" : "need to trace my property",
# "available_days" : "any_day",
# "available_time" : "any_time"
# }


# {
# "property_title" : "xyz",
# "property_type" : "bunglow",
# "property_description" : "need to trace my property location",
# "available_days" : "any_day",
# "available_time" : "any_time",
# "user": 6
# }
