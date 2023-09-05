# import rest_framework
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CustomerSerializer
from customer.models import Customer
from rest_framework import status
from rest_framework import serializers

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
        
# Create your views here.
