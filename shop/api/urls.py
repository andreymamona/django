from django.urls import include, path
from rest_framework import routers
from api.products.views import ProductViewSet, PurchaseViewSet
from api.users.views import RegisterView, LoginView, LogoutView

app_name = "api"

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"purchases", PurchaseViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logoutn"),
]
