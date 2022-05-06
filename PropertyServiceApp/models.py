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
        return self.full_name + " || " + self.phone_number


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
        return self.property_title + " || " + self.property_description


class MaintainanceAndLease(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=0, related_name='maintainance_and_lease')
    property_title = models.CharField(max_length=255, blank=True, null=True)
    property_type = models.CharField(max_length=55, blank=True, null=True)
    property_description = models.CharField(
        max_length=255, blank=True, null=True)
    video = models.TextField(blank=True, null=True)
    virtual_tour = models.TextField(blank=True, null=True)
    available_days = models.JSONField(blank=True, null=True)
    available_time = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.property_title + " || " + self.property_description


class LegalIssues(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=0, related_name='legal_issues')
    issue_type = models.CharField(max_length=255, blank=True, null=True)
    property_type = models.CharField(max_length=55, blank=True, null=True)
    issue_description = models.CharField(
        max_length=255, blank=True, null=True)
    available_days = models.JSONField(blank=True, null=True)
    available_time = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.issue_type + " || " + self.issue_description


class PropertyMonitoring(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=0, related_name='property_monitoring')
    monitoring_type = models.CharField(max_length=255, blank=True, null=True)
    property_type = models.CharField(max_length=55, blank=True, null=True)
    property_description = models.CharField(
        max_length=255, blank=True, null=True)
    available_days = models.JSONField(blank=True, null=True)
    available_time = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.monitoring_type + " || " + self.property_description


class InvestmentAdvice(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=0, related_name='investment_advice')
    property_id = models.CharField(max_length=255, blank=True, null=True)
    property_size = models.CharField(max_length=55, blank=True, null=True)
    land_size = models.CharField(max_length=255, blank=True, null=True)
    beds = models.CharField(max_length=255, blank=True, null=True)
    baths = models.CharField(max_length=255, blank=True, null=True)
    garage = models.CharField(max_length=255, blank=True, null=True)
    garage_size = models.CharField(max_length=255, blank=True, null=True)
    build_year = models.CharField(max_length=255, blank=True, null=True)
    property_features = models.JSONField(blank=True, null=True)
    available_days = models.JSONField(blank=True, null=True)
    available_time = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.property_id + " || " + self.property_size
