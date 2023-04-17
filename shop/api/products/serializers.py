from django.db.models import Sum
from rest_framework import serializers

from products.models import Product, Purchase


class ProductModelSerializer(serializers.HyperlinkedModelSerializer):

    has_image = serializers.SerializerMethodField()
    purchases_count = serializers.IntegerField()

    def get_has_image(self, obj) -> bool:
        return bool(obj.image)

    def get_purchases_count(self, obj) -> int:
        return obj.purchases_count

    class Meta:
        model = Product
        fields = ["title", "has_image", "price", "purchases_count", "image", "description", "created_at"]


class PurchaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['user_id', 'product_id', 'count', 'created_at', 'id']
