import logging
from django.http import HttpResponse
from django.db.models import Avg, Count, Min, Sum, Q, FloatField, Func, F, Value
from django.shortcuts import render
from django.views.generic import ListView
from products.forms import CreateItemForm
from products.models import Product, Purchase
from django_tables2 import SingleTableView
from .tables import ProductTable

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
        products = products.annotate(sales_cost=F("pur_count") * F("price"))
        products = products.filter(sales_cost__gte=1)
        products = products.order_by("sales_cost")

    purchases_count = request.GET.get("sort_sales_num")
    if purchases_count is not None:
        products = products.annotate(pur_count=Sum("purchases__count"))
        products = products.order_by("-pur_count")

    context = {
        "products": products,
    }

    return render(request, "index.html", context)


def additem(request):
    form = CreateItemForm()
    if request.method == "POST":
        form = CreateItemForm(request.POST)
        if form.is_valid():
            product = Product.objects.create(title=form.cleaned_data['title'],
                                             price=form.cleaned_data['price'],
                                             description=form.cleaned_data['description'],
                                             # color=form.cleaned_data['color'],
                                             )
            return HttpResponse(f"Item added :) <br> <p><a href='/'>Main page</a></p>")
        else:
            return HttpResponse(f"Sorry, some data is invalid <br> <p><a href='/'>Main page</a></p>"
                                f"<p><a href='/additem'>Add item</a></p>")
    else:
        form = CreateItemForm()

    return render(request, "additem.html", {"form": form})


def product_info(request):
    item_id = request.GET.get("id")
    try:
        product = Product.objects.get(id=item_id)
    except Product.DoesNotExist:
        return HttpResponse(f"Ooops...wrong ID<br> <p><a href='/'>Main page</a></p>")
    context = {
        "product": product,
    }
    return render(request, "product_info.html", context)
