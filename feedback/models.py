from django.contrib.gis.db import models
from django.utils.translation import ugettext as _
from django.conf import settings 
from django.db.models import F
from search.models import PlaceDetail

class ReviewRating(models.Model):                                    
    
    review_detail = models.TextField(_("Review"),)
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    place = models.ForeignKey(PlaceDetail,db_column='place_id')
    rating = models.DecimalField(_("Rating"),max_digits=2,decimal_places=1)
    
    with_whom = models.CharField(_("With Friend"),max_length=1024,null=True,blank=True)
    tag_friend = models.CharField(_("Tag Friends"),max_length=1024,null=True,blank=True)
    
    location = models.PointField(_("Review Location"),geography=True, srid=4326,help_text="Format:Point(lat lng)")
    
    is_verified = models.BooleanField(_("Review Verified"),default=False)
    is_credited = models.BooleanField(_("Credit on reviews"),default=False)
    is_deleted = models.BooleanField(_("Deleted Review"),default=False)
    
    comment_count = models.IntegerField(_("comment count"),default=0,max_length=100)
    like_count = models.IntegerField(_("like count"),default=0,max_length=100)
    
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    
    class Meta:
        app_label = 'feedback'
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedback')
        ordering = ['-id']
    
    def __unicode__(self):
        return 'place_id:%s,user_id:%s'%(self.place_id,self.owner) 


class Rating(models.Model):
    
    rate = models.CharField(_("Rating"),max_length=10)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    place_id = models.CharField(_("Place ID"), max_length=1024)
    location = models.PointField(_("Rating Location"),geography=True, srid=4326)
    
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
 
    class Meta:
        app_label = 'feedback'
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedback')
        ordering = ['-id']
    
    def __unicode__(self):
        return 'rate:%s,user_id:%s'%(self.rate,self.owner) 

class ReviewComment(models.Model):                            #Date time field
    
    review = models.ForeignKey(ReviewRating,related_name='comment')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    comment = models.TextField(_("Comment"),)
    
    tag_friend = models.CharField(_("Tag Friends"),max_length=1024,null=True,blank=True)
    is_deleted = models.BooleanField(_("Deleted Comment"),default=False)
    like_count = models.IntegerField(_("like count"),default=0,max_length=100)
    
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    
    class Meta:
        app_label = 'feedback'
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedback')
        ordering = ['-id']
    
    def __unicode__(self):
        return 'comment:%s,user_id:%s'%(self.comment,self.owner) 
 
class ReviewLike(models.Model):                                            
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)    
    review = models.ForeignKey(ReviewRating,related_name="like_review")
    
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)

    def __unicode__(self):
        return "review:%s"%(self.review.review_detail)

class CommentLike(models.Model):                                             
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.ForeignKey(ReviewComment,related_name="like_comment")
    
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    

