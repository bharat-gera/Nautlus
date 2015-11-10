from rest_framework import serializers
from order.models import Order
import json

class OrderSerializer(serializers.ModelSerializer):
    
    owner_name = serializers.CharField(source='owner.name',read_only=True)
    owner_email = serializers.CharField(source='owner.email',read_only=True)
    shop_details = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ('id','order_id','owner_name','owner_email','amount','date_added','shop_details','type')
        
    def get_shop_details(self,obj): 
        return json.dumps(str(obj.content_object))        