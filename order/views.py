from django.shortcuts import render
from rest_framework import generics
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework import permissions

class OrderDetail(generics.ListAPIView):
    """
     Total No. of orders that has been placed by the login user.
    """
    model = Order
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)    
    
    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)
