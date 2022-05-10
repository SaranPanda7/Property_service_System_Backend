from itertools import count
import time
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


def create_property_tracing_servId():
    prefix = "PSS-PT-00"
    data = PropertyTracing.objects.filter(
        service_name="propertyTracing").values_list('sno', flat=True)

    if data.count() < 1:
        return("PSS-PT-001")

    elif data.count() > 0:
        suffix = str(max(data)+1)
        service_id = prefix + str(suffix)
        return(service_id)


def pt_records_count():
    data = PropertyTracing.objects.count() + 1
    return(data)


class PropertyTracing(models.Model):
    sno = models.IntegerField(default=pt_records_count)
    service_id = models.CharField(max_length=20,
                                  primary_key=True, default=create_property_tracing_servId)
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=0, related_name='property_tracing')
    service_name = models.CharField(max_length=55, default="propertyTracing")

    property_title = models.CharField(max_length=255, blank=True, null=True)
    property_type = models.CharField(max_length=55, blank=True, null=True)
    property_description = models.CharField(
        max_length=255, blank=True, null=True)
    available_days = models.JSONField(blank=True, null=True)
    available_time = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.service_id + " || " + self.property_title + " || " + self.property_description


def create_maintainaceLease_servId():
    prefix = "PSS-ML-00"
    data = MaintainanceAndLease.objects.filter(
        service_name="maintainanceAndLease").values_list('sno', flat=True)

    if data.count() < 1:
        return("PSS-ML-001")

    elif data.count() > 0:
        suffix = str(max(data)+1)
        service_id = prefix + str(suffix)
        return(service_id)


def ml_records_count():
    data = MaintainanceAndLease.objects.count() + 1
    return(data)


class MaintainanceAndLease(models.Model):
    sno = models.IntegerField(default=ml_records_count)
    service_id = models.CharField(max_length=20,
                                  primary_key=True, default=create_maintainaceLease_servId)
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=0, related_name='maintainance_and_lease')
    service_name = models.CharField(
        max_length=55, default="maintainanceAndLease")
    property_title = models.CharField(max_length=255, blank=True, null=True)
    property_type = models.CharField(max_length=55, blank=True, null=True)
    property_description = models.CharField(
        max_length=255, blank=True, null=True)
    video = models.TextField(blank=True, null=True)
    virtual_tour = models.TextField(blank=True, null=True)
    available_days = models.JSONField(blank=True, null=True)
    available_time = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.service_id + " || " + self.property_title + " || " + self.property_description


def create_legalIssues_servId():
    prefix = "PSS-LI-00"
    data = LegalIssues.objects.filter(
        service_name="legalIssues").values_list('sno', flat=True)

    if data.count() < 1:
        return("PSS-LI-001")

    elif data.count() > 0:
        suffix = str(max(data)+1)
        service_id = prefix + str(suffix)
        return(service_id)


def li_records_count():
    data = LegalIssues.objects.count() + 1
    return(data)


class LegalIssues(models.Model):
    sno = models.IntegerField(default=li_records_count)
    service_id = models.CharField(max_length=20,
                                  primary_key=True, default=create_legalIssues_servId)
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=0, related_name='legal_issues')
    service_name = models.CharField(
        max_length=55, default="legalIssues")
    issue_type = models.CharField(max_length=255, blank=True, null=True)
    property_type = models.CharField(max_length=55, blank=True, null=True)
    issue_description = models.CharField(
        max_length=255, blank=True, null=True)
    available_days = models.JSONField(blank=True, null=True)
    available_time = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.service_id + " || " + self.issue_type + " || " + self.issue_description


def create_propertyMonitoring_servId():
    prefix = "PSS-PM-00"
    data = PropertyMonitoring.objects.filter(
        service_name="propertyMonitoring").values_list('sno', flat=True)

    if data.count() < 1:
        return("PSS-PM-001")

    elif data.count() > 0:
        suffix = str(max(data)+1)
        service_id = prefix + str(suffix)
        return(service_id)


def pm_records_count():
    data = PropertyMonitoring.objects.count() + 1
    return(data)


class PropertyMonitoring(models.Model):
    sno = models.IntegerField(default=pm_records_count)
    service_id = models.CharField(max_length=20,
                                  primary_key=True, default=create_propertyMonitoring_servId)
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=0, related_name='property_monitoring')
    service_name = models.CharField(
        max_length=55, default="propertyMonitoring")
    monitoring_type = models.CharField(max_length=255, blank=True, null=True)
    property_type = models.CharField(max_length=55, blank=True, null=True)
    property_description = models.CharField(
        max_length=255, blank=True, null=True)
    available_days = models.JSONField(blank=True, null=True)
    available_time = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.service_id + " || " + self.monitoring_type + " || " + self.property_description


def create_investmentAdvice_servId():
    prefix = "PSS-IA-00"
    data = InvestmentAdvice.objects.filter(
        service_name="investmentAdvice").values_list('sno', flat=True)

    if data.count() < 1:
        return("PSS-IA-001")

    elif data.count() > 0:
        suffix = str(max(data)+1)
        service_id = prefix + str(suffix)
        return(service_id)


def ia_records_count():
    data = InvestmentAdvice.objects.count() + 1
    return(data)


class InvestmentAdvice(models.Model):
    sno = models.IntegerField(default=ia_records_count)
    service_id = models.CharField(max_length=20,
                                  primary_key=True, default=create_investmentAdvice_servId)
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=0, related_name='investment_advice')
    service_name = models.CharField(
        max_length=55, default="investmentAdvice")
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
        return self.service_id + " || " + self.property_id + " || " + self.property_size


def create_otherServices_servId():
    prefix = "PSS-OS-00"
    data = OtherServices.objects.filter(
        service_name="otherServices").values_list('sno', flat=True)

    if data.count() < 1:
        return("PSS-OS-001")

    elif data.count() > 0:
        suffix = str(max(data)+1)
        service_id = prefix + str(suffix)
        return(service_id)


def os_records_count():
    data = OtherServices.objects.count() + 1
    return(data)


class OtherServices(models.Model):
    sno = models.IntegerField(default=os_records_count)
    service_id = models.CharField(max_length=20,
                                  primary_key=True, default=create_otherServices_servId)
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=0, related_name='other_service')
    service_name = models.CharField(
        max_length=55, default="otherServices")
    required_service = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city_name = models.CharField(max_length=55, blank=True, null=True)
    state = models.CharField(max_length=55, blank=True, null=True)
    pin_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    address_type = models.CharField(max_length=30, blank=True, null=True)
    available_days = models.JSONField(blank=True, null=True)
    available_time = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.service_id + " || " + self.required_service + " || " + self.city_name
