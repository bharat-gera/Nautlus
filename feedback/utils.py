from django.conf import settings
from wallet.models import Wallet
import random

def order_generation(object_id):
    rand_no = ''.join(random.choice('0123456789ABCDEFGHIJKL') for i in range(4))
    order_no = rand_no + str(object_id)
    return order_no

class BusinessRating(object):
    

    def review_amount(self,obj):
        num_char = len((obj.review_detail).replace(" ",""))
        if num_char < settings.MAX_REVIEW_LENGTH: 
            amt = (num_char*settings.CHAR_PRICE)/float(100)               #in rs
            points = int(round(num_char/settings.ONE_POINT_CHARS))
        else:
            amt = (settings.MAX_REVIEW_LENGTH*settings.CHAR_PRICE)/float(100)
            points = int(round(settings.MAX_REVIEW_LENGTH/settings.ONE_POINT_CHARS))        
        return amt,points
    
    def user_wallet(self,obj):
        obj_wallet,created = Wallet.objects.get_or_create(owner=obj.owner)
        amt,point = self.review_amount(obj)
        if created:
            return Wallet(owner=obj.owner,amount=amt,level=0,point=point).save()
        total_point,amount = obj_wallet.point + point,float(obj_wallet.amount) + amt
        level = int(total_point/settings.LEVEL_UP)
        if obj_wallet.level < level:
            amount = amount + settings.LEVEL_UP_BONUS
        obj_wallet.level = level
        obj_wallet.amount = amount
        obj_wallet.point = total_point
        obj_wallet.save() 
        obj.is_credited = True
        return obj.save()
