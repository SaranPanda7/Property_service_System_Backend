from pyexpat import model
from rest_framework import serializers
from .models import Roles, Users, PropertyTracing, MaintainanceAndLease, LegalIssues, PropertyMonitoring, InvestmentAdvice


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        # fields = '__all__'
        fields = ['id', 'role']


class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()

    class Meta:
        model = Users
        fields = ['id', 'phone_number',
                  'full_name', 'email', 'address', 'role']
        # fields = '__all__'


class GetAllPropertyTracingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyTracing
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
