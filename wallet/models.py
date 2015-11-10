from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _ 


class Wallet(models.Model):
    
    owner = models.OneToOneField(settings.AUTH_USER_MODEL)
    level = models.IntegerField(_("User Level"),default=0)
    point = models.IntegerField(_("User Points"),default=0)
    amount = models.FloatField(_("User's credit"),default=0)
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    
    def __unicode__(self):
        return "credit:%d"%(self.amount)

class Recharge(models.Model):
    
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    amount = models.IntegerField(_("Recharge Amount"))
    operator = models.CharField(_("Operator"),max_length=64)
    mobile_number = models.CharField(_("Mobile Number"),max_length=10)
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    is_recharged = models.BooleanField(default=False)
    
    def __unicode__(self):
        return ("amount:%d,mobile_number:%s,operator:%s,date_added:%s"%(self.amount,\
                                                          self.mobile_number,self.operator,self.date_added))
    
        
    