from rest_framework import serializers
from wallet.models import Recharge,Wallet
from django.shortcuts import get_object_or_404

class WalletSerializer(serializers.ModelSerializer):
    
    owner_name = serializers.CharField(source='owner.name',read_only=True)
    owner_eamil = serializers.CharField(source='owner.email',read_only=True)
    
    class Meta:
        model = Wallet
        fileds=('id','owner_name','owner_email','amount','point','level',)

class RechargeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recharge
        fields = ('id','mobile_number','amount','operator',)
        
    def validate_amount(self,value):
        wallet_obj = get_object_or_404(Wallet,owner_id=self.context['request'].user.id)
        if wallet_obj.amount>= value:
            wallet_obj.amount = wallet_obj.amount - value
            wallet_obj.save()  
            return value
        raise serializers.ValidationError("Insufficient Amount in Wallet")
    
