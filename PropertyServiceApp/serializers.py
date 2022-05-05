from pyexpat import model
from rest_framework import serializers
from .models import Roles, Users, PropertyTracing


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
