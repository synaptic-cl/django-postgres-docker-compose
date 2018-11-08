from rest_framework import viewsets

from main.models import Product, Family, Location
from main.serializers import ProductSerializer, FamilySerializer, LocationSerializer


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('-sku')


class FamilyViewset(viewsets.ModelViewSet):
    serializer_class = FamilySerializer
    queryset = Family.objects.all().order_by('-id')


class LocationViewset(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all().order_by('-id')
