from api.products.views import (ProductViewSet, PurchaseViewSet,
                                TheMostExpensiveProductViewSet,
                                TheMostPopularProductViewSet)
from api.users.views import LoginView, LogoutView, RegisterView
from rest_framework import routers

from django.urls import include, path

app_name = "api"

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"purchases", PurchaseViewSet)


urlpatterns = [
    path(
        "products/expensive/",
        TheMostExpensiveProductViewSet.as_view(),
        name="products_expensive",
    ),
    path(
        "products/popular/",
        TheMostPopularProductViewSet.as_view(),
        name="products_popular",
    ),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logoutn"),
    path("", include(router.urls)),
]
