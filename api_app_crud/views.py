from copy import error
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product
# Create your views here.


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-delete/<int:id>',
    }

    return Response(api_urls)


@api_view(['GET'])
def show_products(request):
    product_queryset = Product.objects.all()
    serializer = ProductSerializer(product_queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def show_product_detail(request, pk):
    product_queryset = Product.objects.get(id=pk)
    serializer = ProductSerializer(product_queryset, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def update_product(request, pk):
    product_queryset = Product.objects.get(id=pk)
    serializer = ProductSerializer(
        product_queryset, many=False, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_product(request, pk):
    product_queryset = Product.objects.get(id=pk)
    product_queryset.delete()
    return Response('Product deleted successfully')
