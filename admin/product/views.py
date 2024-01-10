from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
# product/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
    @swagger_auto_schema(operation_description="List all products")
    def list(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductSerializer, responses={201: ProductSerializer()})
    def create(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self,request,pk=None):
        try:
            product = Product.objects.get(product_id=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

