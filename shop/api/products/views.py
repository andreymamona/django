from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from api.products.serializers import (
    ProductModelSerializer,
    PurchaseModelSerializer,
    ProductSerializer,
)
from products.models import Product, Purchase


class ProductViewSet(viewsets.ModelViewSet):
    queryset = (
        Product.objects.all()
        .annotate(purchases_count=Sum("purchases__count"))
        .order_by("-created_at")
    )
    serializer_class = ProductModelSerializer
    permission_classes = []


class TheMostExpensiveProductViewSet(ListAPIView):
    queryset = Product.objects.all().order_by("-price")
    serializer_class = ProductSerializer
    permission_classes = []


class TheMostPopularProductViewSet(ListAPIView):
    queryset = (
        Product.objects.all()
        .annotate(purchases_count=Sum("purchases__count", default=0))
        .order_by("-purchases_count")
    )
    serializer_class = ProductSerializer
    permission_classes = []


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all().order_by("-created_at")
    serializer_class = PurchaseModelSerializer
    permission_classes = []
