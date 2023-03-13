import logging
from django.http import HttpResponse
from django.db.models import Avg, Count, Min, Sum, Q, FloatField, Func, F, Value
from django.shortcuts import render

from products.models import Product, Purchase

logger = logging.getLogger(__name__)


def index(request):
    products = Product.objects.all()

    title = request.GET.get("title")
    if title is not None:
        products = products.filter(title__icontains=title)

    purchases__count = request.GET.get("count")
    if purchases__count is not None:
        products = products.filter(purchases__count__gte=purchases__count)

    sort_price = request.GET.get("sort_price")
    if sort_price is not None:
        if sort_price == 'up':
            products = products.order_by("price")
        elif sort_price == 'down':
            products = products.order_by("-price")

    sort_sales_cost = request.GET.get("sort_sales_cost")
    if sort_sales_cost is not None:
        products = products.annotate(pur_count=Sum("purchases__count"))
        products = products.annotate(sales_cost=F("pur_count")*F("price"))
        products = products.filter(sales_cost__gte=1)
        products = products.order_by("sales_cost")
        string = ''
        for p in products:
            string += f"<br>{str(p)} x {p.pur_count} = {p.sales_cost}"
        return HttpResponse(string)

    purchases_count = request.GET.get("sort_sales_num")
    if purchases_count is not None:
        products = products.annotate(pur_count=Sum("purchases__count"))
        products = products.order_by("pur_count")
        string = ''
        for p in products:
            string += f"<br>{str(p)} Purchases: {p.pur_count}"
        return HttpResponse(string)

    string = f"<br>".join([str(p) for p in products])
    return HttpResponse(string)
