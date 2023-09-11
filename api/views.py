# import rest_framework
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomerSerializer,ProductSerializer,CartSerializer,OrderSerializer
from customer.models import Customer
from rest_framework import status
from rest_framework import serializers
from inventory.models import Product
from cart.models import Product_Cart
from order.models import Order



class CustomerListView(APIView):

    def get(self,request):
       customer = Customer.objects.all()
       serializer = CustomerSerializer(customer,many=True)
       return Response(serializer.data , status=status.HTTP_200_OK)

    def post(self,request):
        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400)    


class CustomerDetailView(APIView):

    def get(self,request,id,format=None):
         customer=Customer.objects.get(id=id)
         serializer=CustomerSerializer(customer)
         return Response(serializer.data)

    def put(self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        serializer=CustomerSerializer(customer,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors,status=status.HTTP_400)  

    def delete(self,request,id,format=None):
        customer=customer.objects.get(id=id)
        customer.delete()
        return Response("customer Deleted", status=status.HTTP_204_No_CONTENT)

class ProductListView(APIView):

    def get(self,request):
       product = Product.objects.all()
       serializer = ProductSerializer(product,many=True)
       return Response(serializer.data , status=status.HTTP_200_OK)

    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400)    


class ProductDetailView(APIView):

    def get(self,request,id,format=None):
         product=Product.objects.get(id=id)
         serializer=ProductSerializer(product)
         return Response(serializer.data)

    def put(self,request,id,format=None):
        product=Product.objects.get(id=id)
        serializer=ProductSerializer(product,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors,status=status.HTTP_400)  

    def delete(self,request,id,format=None):
        product=Product.objects.get(id=id)
        product.delete()
        return Response(" product Deleted", status=status.HTTP_204_No_CONTENT)   


        
class CartListView(APIView):

    def get(self,request):
       cart=Product_Cart.objects.all()
       serializer = CartSerializer(cart,many=True)
       return Response(serializer.data , status=status.HTTP_200_OK)

    def post(self,request):
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400)    


class CartDetailView(APIView):

    def get(self,request,id,format=None):
         cart=Product_Cart.objects.get(id=id)
         serializer=CartSerializer(cart)
         return Response(serializer.data)

    def put(self,request,id,format=None):
        cart=Product_Cart.objects.get(id=id)
        serializer=CartSerializer(cart,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors,status=status.HTTP_400)  

    def delete(self,request,id,format=None):
        cart=Product_Cart.objects.get(id=id)
        cart.delete()
        return Response(" Cart Deleted", status=status.HTTP_204_No_CONTENT)    

        
class OrderListView(APIView):

    def get(self,request):
       order = Order.objects.all()
       serializer = OrderSerializer(order,many=True)
       return Response(serializer.data , status=status.HTTP_200_OK)

    def post(self,request):
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400)    


class OrderDetailView(APIView):

    def get(self,request,id,format=None):
         order=Order.objects.get(id=id)
         serializer=OrderSerializer()
         return Response(serializer.data)

    def put(self,request,id,format=None):
        order=Order.objects.get(id=id)
        serializer=OrderSerializer(order,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors,status=status.HTTP_400)  

    def delete(self,request,id,format=None):
        order=Order.objects.get(id=id)
        order.delete()
        return Response(" Order Deleted", status=status.HTTP_204_No_CONTENT)     
 
  


        
# class AddtoCartView(APIView)      :
#      def post(self,request,id,format=None):
#         cart_id=request.datag["cart_id"]
#         product_id=request.datag["product_id"]
#         cart=Cart.objects.get(id=cart_id)
#         product=Product.objects.get(id=product_id)
#         updated_cart=Cart.add_product(product)
#         serializer=CartSerializer(updated_cart)
#         return Response(serializer.data)   
        
# Create your views here.
