from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import *


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'
        # fields = ['id', 'role']


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = Users
        fields = '__all__'
        # fields = ['id', 'phone_number',
        #           'full_name', 'email', 'address', 'role']


class ServicesSupportUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'full_name', 'phone_number']


class GetAllPropertyTracingSerializer(serializers.ModelSerializer):
    user = ServicesSupportUserSerializer()

    class Meta:
        model = PropertyTracing
        fields = '__all__'


class GetAllMaintainanceAndLeaseSerializer(serializers.ModelSerializer):
    user = ServicesSupportUserSerializer()

    class Meta:
        model = MaintainanceAndLease
        fields = '__all__'


class GetAllLegalIssuesSerializer(serializers.ModelSerializer):
    user = ServicesSupportUserSerializer()

    class Meta:
        model = LegalIssues
        fields = '__all__'


class GetAllPropertyMonitoringSerializer(serializers.ModelSerializer):
    user = ServicesSupportUserSerializer()

    class Meta:
        model = PropertyMonitoring
        fields = '__all__'


class GetAllInvestmentAdviceSerializer(serializers.ModelSerializer):
    user = ServicesSupportUserSerializer()

    class Meta:
        model = InvestmentAdvice
        fields = '__all__'


class GetAllOtherServicesSerializer(serializers.ModelSerializer):
    user = ServicesSupportUserSerializer()

    class Meta:
        model = OtherServices
        fields = '__all__'


class AddPropertyTracingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyTracing
        fields = '__all__'


class AddMaintainanceAndLeaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaintainanceAndLease
        fields = '__all__'


class AddLegalIssuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = LegalIssues
        fields = '__all__'


class AddPropertyMonitoringSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyMonitoring
        fields = '__all__'


class AddInvestmentAdviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvestmentAdvice
        fields = '__all__'


class AddOtherServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = OtherServices
        fields = '__all__'
