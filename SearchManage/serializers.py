from rest_framework import serializers
from SearchManage.models import *


class DrugCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugCountry
        # fields = '__all__'
        fields = ['country_id', 'year', 'num']
        # id = serializers.IntegerField()
        # name = serializers.CharField(source='drug_name')
        # eng_name = serializers.CharField(source='drug_eng_name')
        # desc = serializers.CharField(source='drug_desc')


class DrugAgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugAge
        # fields = '__all__'
        fields = ['age_id', 'country_id', 'year', 'num']


class DrugGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugGender
        # fields = '__all__'
        fields = ['gender_id', 'country_id', 'year', 'num']


class DrugTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugType
        # fields = '__all__'
        fields = ['drug_id', 'country_id', 'year', 'num']
