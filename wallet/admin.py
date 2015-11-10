from django.contrib import admin
from wallet.models import Recharge,Wallet
from order.models import Order
from feedback.utils import order_generation

class WalletAdmin(admin.ModelAdmin):
    
    date_hierarchy = 'date_added'
    list_display = ('id','owner_name','owner_email','level','point','amount','date_added','last_modified',)
    readonly_fields = ('level','point','amount','date_added','last_modified','owner')   
    actions = None
    
    def owner_name(self,obj):
        return obj.owner.name
    owner_name.short_description = 'Owner Name'
    
    def owner_email(self,obj):
        return obj.owner.email
    owner_email.short_description = 'Owner Email'
    
    def has_delete_permission(self,request,obj=None):
        return False
    def has_add_permission(self, request):
        return False

class RechargeAdmin(admin.ModelAdmin):

    date_hierarchy = 'date_added'
    list_display = ('id','owner_name','owner_email','amount','operator','mobile_number','date_added','last_modified','is_recharged',)
    readonly_fields = ('owner','amount','operator','mobile_number','date_added','last_modified',)
    actions = ['recharge_request_completed']
    
    def recharge_request_completed(self,request,queryset):
        for obj in queryset:
            if not obj.is_recharged:
                Order(owner=obj.owner,order_id=order_generation(obj.id),content_object=obj,amount=obj.amount,).save()
                obj.is_recharged = True
                obj.save()
                self.message_user(request,"Request for recharge from user_email:%s is completed"%(obj.owner.email))
            else:
                self.message_user(request,"Perhaps request for recharge from user_email:%s is already completed"%(obj.owner.email))
    recharge_request_completed.short_description = "Mark Recharge Request Completed"
    
    def get_actions(self,request):
        actions = super(RechargeAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions 
    
    def owner_name(self,obj):
        return obj.owner.name
    owner_name.short_description = 'Owner Name'
    
    def owner_email(self,obj):
        return obj.owner.email
    owner_email.short_description = 'Owner Email'
    
    def has_delete_permission(self,request,obj=None):
        return False
    def has_add_permission(self, request):
        return False

        
admin.site.register(Wallet,WalletAdmin)
admin.site.register(Recharge,RechargeAdmin)    

