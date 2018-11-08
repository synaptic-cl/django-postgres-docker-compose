from rest_framework import serializers
from main.models import Product, Family, Location


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
