from rest_framework import serializers
from catalogApp.models import Product, Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name', 'slug']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'slug', 'category_id']