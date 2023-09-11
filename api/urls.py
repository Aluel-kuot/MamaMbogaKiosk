from django.urls import path
from .views import CustomerListView
from .views import CustomerDetailView
from .views import ProductDetailView
from .views import ProductListView
from .views import CartDetailView
from .views import CartListView
from .views import OrderDetailView
from .views import OrderListView


urlpatterns =[
    path("customers/",CustomerListView.as_view(), name = "customer_list_view"),
    path("customer/<int:id>/",CustomerDetailView.as_view(), name="customer_detail_view"),
    # path("add_to_cart/",AddToCartView.as_view(), name="add_to_cart"),
    path("products/",ProductListView.as_view(), name = "product_list_view"),
    path("product/<int:id>/",ProductDetailView.as_view(), name="product_detail_view"),
    path("carts/",CartListView.as_view(), name = "cart_list_view"),
    path("cart/<int:id>/",CartDetailView.as_view(), name="cart_detail_view"),
    path("orders/",OrderListView.as_view(), name = "order_list_view"),
    path("order/<int:id>/",OrderDetailView.as_view(), name="order_detail_view"),


]