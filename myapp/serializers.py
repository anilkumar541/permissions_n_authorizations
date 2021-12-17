from rest_framework import serializers
from myapp.models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["id","product_name", "category", "created_at", "updated_at"]        

class CategorySerializer(serializers.ModelSerializer):
    product=ProductSerializer(many=True, read_only=True)
    class Meta:
        model=Category
        fields=["id","category_name", "product","created_at", "updated_at"]


