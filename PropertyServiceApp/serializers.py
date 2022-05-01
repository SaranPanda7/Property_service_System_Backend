from rest_framework import serializers
from .models import Roles, Users


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        # fields = '__all__'
        fields = ['id', 'role']


class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()
    class Meta:
        model = Users
        fields = ['id', 'phone_number', 'full_name', 'email', 'address', 'role']
        # fields = '__all__'
