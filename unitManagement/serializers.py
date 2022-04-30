from rest_framework import serializers
from .models import Address, Leasing_Info, UnitType, Community, Unit

class Leasing_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Leasing_Info
        fields = '__all__' 

class Address_Serializer(serializers.ModelSerializer):
    class Meta:
        model =  Address
        fields = '__all__' 

class Unit_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UnitType
        fields = '__all__' 

class Community_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__' 

class Unit_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'