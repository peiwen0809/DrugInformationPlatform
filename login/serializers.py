from rest_framework import serializers
from login.models import Admin


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['account', 'password']
