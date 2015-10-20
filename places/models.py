from django.db import models
from django.conf import settings 
from django.utils.translation import ugettext as _

class Bookmarked(models.Model):
    
    place_id = models.CharField(_("Place ID"),max_length=128)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    
    class Meta:
        app_label = 'places'
        verbose_name = _('Place')
        verbose_name_plural = _('Places')
        ordering = ['-id']
    
    def __unicode__(self):
        return 'place_id:%s,user_id:%s'%(self.place_id,self.owner)
    
class Beenhere(models.Model):
    
    place_id = models.CharField(_("Been Here"),max_length=128)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    
    class Meta:
        app_label = 'places'
        verbose_name = _('Place')
        verbose_name_plural = _('Places')
        ordering = ['-id']
    
    def __unicode__(self):
        return 'place_id:%s,user_id:%s'%(self.place_id,self.owner)

    
class Favourites(models.Model):        
    
    place_id = models.CharField(_("Been Here"),max_length=128)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    
    class Meta:
        app_label = 'places'
        verbose_name = _('Place')
        verbose_name_plural = _('Places')
        ordering = ['-id']
    
    def __unicode__(self):
        return 'place_id:%s,user_id:%s'%(self.place_id,self.owner)
