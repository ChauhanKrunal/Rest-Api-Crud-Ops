from django.db import models
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'