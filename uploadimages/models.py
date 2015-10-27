from django.contrib.gis.db import models
from django.utils.translation import ugettext as _
from django.conf import settings 
from django.db.models import F
from search.models import PlaceDetail

class UploadImage(models.Model):                                                
    
    place = models.ForeignKey(PlaceDetail,db_column='place_id',related_name='place_image')
    review = models.ForeignKey('feedback.ReviewRating',null=True)
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True)
    
    image = models.ImageField(_("Image"),upload_to="upload_images",null=True)
    google_images = models.TextField(_("Google Images"),null=True)
    review_images = models.ImageField(_("Review Image"),upload_to="upload_images",null=True)
    
    tag_friend = models.CharField(_("Tag Friends"),max_length=1024,null=True,blank=True)
    special_feature = models.TextField(_("Special Feature"),max_length=1024,null=True,blank=True)
    location = models.PointField(_("Review Location"),geography=True, srid=4326)
    
    is_verified = models.BooleanField(_("Upload Image Verified"),default=False)
    is_credited = models.BooleanField(_("Credit on Uploaded Image"),default=False)
    
    comment_count = models.IntegerField(_("comment count"),default=0,max_length=100)
    like_count = models.IntegerField(_("like count"),default=0,max_length=100)
    with_whom = models.CharField(_("With Friend"),max_length=1024,null=True,blank=True)
    is_deleted = models.BooleanField(_("Deleted Image"),default=False)
    
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    
    class Meta:
        app_label = 'uploadimages'
        verbose_name = _('UploadImage')
        verbose_name_plural = _('UploadImages')
        ordering = ['-id']
    
    def __unicode__(self):
        return 'image:%s,user_id:%s'%(self.image,self.owner) 
    
class ImageComment(models.Model):
    
    upload_image = models.ForeignKey(UploadImage,related_name="image_comment")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    comment = models.TextField(_("Comment"),)     
    
    tag_friend = models.CharField(_("Tag Friends"),max_length=1024,null=True,blank=True)
    like_count = models.IntegerField(_("like count"),default=0,max_length=100)
    is_deleted = models.BooleanField(_("Deleted Comment"),default=False)
    
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    
    class Meta:
        app_label = 'uploadimages'
        verbose_name = _('ImageComment')
        verbose_name_plural = _('ImageComments')
        ordering = ['-id']
    
    def __unicode__(self):
        return 'comment:%s,user_id:%s'%(self.comment,self.owner) 

class ImageLike(models.Model):
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)    
    upload_image = models.ForeignKey(UploadImage,related_name="like_image")
    
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)

class ImageCommentLike(models.Model):
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    image_comment = models.ForeignKey(ImageComment,related_name="like_image_comment")
    
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
