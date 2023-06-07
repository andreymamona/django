import logging

from products.forms import CreateItemForm
from products.models import Product

from django.db.models import F, Sum
from django.http import HttpResponse
from django.shortcuts import render

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
        if sort_price == "up":
            products = products.order_by("price")
        elif sort_price == "down":
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
    CreateItemForm()
    if request.method == "POST":
        form = CreateItemForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data["title"],
                price=form.cleaned_data["price"],
                description=form.cleaned_data["description"],
                # color=form.cleaned_data['color'],
            )
            return HttpResponse("Item added :) <br> <p><a href='/'>Main page</a></p>")
        else:
            return HttpResponse(
                "Sorry, some data is invalid <br> <p><a href='/'>Main page</a></p>"
                "<p><a href='/additem'>Add item</a></p>"
            )
    else:
        form = CreateItemForm()

    return render(request, "additem.html", {"form": form})


def product_info(request):
    item_id = request.GET.get("id")
    try:
        product = Product.objects.get(id=item_id)
    except Product.DoesNotExist:
        return HttpResponse("Ooops...wrong ID<br> <p><a href='/'>Main page</a></p>")
    context = {
        "product": product,
    }
    return render(request, "product_info.html", context)
