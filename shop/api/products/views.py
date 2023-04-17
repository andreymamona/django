from django.db.models import Sum
from rest_framework import viewsets

from api.products.serializers import ProductModelSerializer, PurchaseModelSerializer
from products.models import Product, Purchase


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed.
    """
    queryset = Product.objects.all().annotate(purchases_count=Sum("purchases__count")).order_by("-created_at")
    serializer_class = ProductModelSerializer
    permission_classes = []


class PurchaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed.
    """
    queryset = Purchase.objects.all().order_by("-created_at")
    serializer_class = PurchaseModelSerializer
    permission_classes = []
