from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from catalogAPI.serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
# Create your views here.



class ShowProductView(APIView):
    def get(self, request):
        products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)
        
        return Response(serializer.data)


class ShowCategoryView(APIView):
    def get(self, request):
            category = Category.objects.all()

            serializer = CategorySerializer(category, many=True)

            return Response(serializer.data)
    


class ProductView(APIView):
    def post(self, request):
        serialiazer = ProductSerializer(data=request.data)

        if serialiazer.is_valid():
             serialiazer.save()
             return Response({"detail": serialiazer.data})
        return Response(serialiazer.errors)


class CategoryView(APIView):
    def post(self, request):
            serializer = CategorySerializer(data=request.data)

            if serializer.is_valid():
                 serializer.save()
                 return Response({"detail": serializer.data})
            
            return Response(serializer.errors)
    



# {"name": "Cow milk", "price": "25.2", "description": "Some cow milk", "slug": "cow-milk", category: ""}


