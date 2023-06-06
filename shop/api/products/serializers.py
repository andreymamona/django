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
        fields = [
            "title",
            "has_image",
            "price",
            "purchases_count",
            "image",
            "description",
            "created_at",
        ]


class PurchaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ["user_id", "product_id", "count", "created_at", "id"]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    external_id = serializers.CharField(
        max_length=255, allow_blank=True, allow_null=True
    )
    title = serializers.CharField(max_length=255)
    price = serializers.FloatField(default=0)
    image = serializers.ImageField(
        allow_empty_file=True, allow_null=True, default="image_item_default.png"
    )
    description = serializers.CharField(allow_blank=True, allow_null=True)
    category = serializers.CharField(allow_blank=True, allow_null=True)
    created_at = serializers.DateTimeField()
    purchases_count = serializers.IntegerField()

    class Meta:
        model = Product
        fields = [
            "title",
            "purchases_count",
            "price",
            "image",
            "description",
            "category",
            "external_id",
            "created_at",
        ]
