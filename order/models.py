from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Order(models.Model):
    
    ORDER_TYPES = (
                   ('recharge',_('Recharge')),
                   
                   )
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL) 
    order_id = models.CharField(_("Order ID"),max_length=128)
    amount = models.FloatField(_("User's Shop"))
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    type = models.CharField(_("Shop Type"),max_length=64,choices=ORDER_TYPES)
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    
    def __unicode__(self):
        return ("order id:%s,owner_id:%s"%(self.order_id,self.owner_id)) 