from rest_framework import serializers

from products.models import Product


class ProductModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "price", "image", "description", "color", "created_at"]

