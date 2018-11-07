# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime


class Product(models.Model):
    sku = models.CharField(
      max_length=13, help_text="Enter Product Stock Keeping Unit")
    barcode = models.CharField(
      max_length=13, help_text="Enter Product Barcode (ISBN, UPC ...)")
    title = models.CharField(max_length=200, help_text="Enter Product Title")
    description = models.TextField(help_text="Enter Product Description")
    unitCost = models.FloatField(help_text="Enter Product Unit Cost")
    unit = models.CharField(max_length=10, help_text="Enter Product Unit ")
    quantity = models.FloatField(help_text="Enter Product Quantity")
    minQuantity = models.FloatField(help_text="Enter Product Min Quantity")
    family = models.ForeignKey('Family', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(default=datetime.datetime.now())

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Product.
        """
        return reverse('product-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.title


class Family(models.Model):
    reference = models.CharField(
      max_length=13, help_text="Enter Family Reference")
    title = models.CharField(max_length=200, help_text="Enter Family Title")
    description = models.TextField(help_text="Enter Family Description")
    unit = models.CharField(max_length=10, help_text="Enter Family Unit ")
    minQuantity = models.FloatField(help_text="Enter Family Min Quantity")

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Family.
        """
        return reverse('family-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.title


class Location(models.Model):
    reference = models.CharField(
      max_length=20, help_text="Enter Location Reference")
    title = models.CharField(max_length=200, help_text="Enter Location Title")
    description = models.TextField(help_text="Enter Location Description")

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Location.
        """
        return reverse('family-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.title
