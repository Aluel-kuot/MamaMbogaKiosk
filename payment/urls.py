from django.urls import path
from .views import payment_create_view


urlpatterns = [
    path('products/upload',payment_create_view, name="payment_create_view"),
   
]