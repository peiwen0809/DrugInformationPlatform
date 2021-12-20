from rest_framework import serializers
from BaseTableSearch.models import *

class AgeTableSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeTableSearch
        fields = '__all__'

class GenderTableSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderTableSearch
        fields = '__all__'
