from wallet.models import Recharge,Wallet
from rest_framework import generics
from django.shortcuts import get_object_or_404
from person.models import Person
from serializers import WalletSerializer,RechargeSerializer
from rest_framework import permissions

class WalletDetail(generics.ListAPIView):
    
    """
    Login for wallet information
    """
    model = Wallet
    serializer_class = WalletSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        
        return self.model.objects.filter(owner=self.request.user)

class RechargeRequest(generics.CreateAPIView):
    
    """
     Request for Recharge Mobile
    """
    model = Recharge
    serializer_class = RechargeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)        