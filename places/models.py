from django.db import models
from django.conf import settings 
from django.utils.translation import ugettext as _
from search.models import PlaceDetail
class Bookmarked(models.Model):
    
    place = models.ForeignKey(PlaceDetail,db_column='place_id')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_marked = models.BooleanField(default=True)
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
    
    place = models.ForeignKey(PlaceDetail,db_column='place_id')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_here = models.BooleanField(default=True)
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
    
    place = models.ForeignKey(PlaceDetail,db_column='place_id')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_fav = models.BooleanField(default=True)
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    
    class Meta:
        app_label = 'places'
        verbose_name = _('Place')
        verbose_name_plural = _('Places')
        ordering = ['-id']
    
    def __unicode__(self):
        return 'place_id:%s,user_id:%s'%(self.place_id,self.owner)
    
class FollowFriends(models.Model):
    
    following = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='following')
    follower = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='follower')
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    
        
        
        
        
    
