from django.contrib.gis.db import models
from django.utils.translation import ugettext as _

class PrimaryCategory(models.Model):

    primary_name = models.CharField(_("Primary Name"),max_length=128,unique=True)
    description = models.TextField(_("Category Desc"),)
    is_active = models.BooleanField(_("Active Category"),default=True)
    image = models.ImageField(_("Image"),upload_to='primary_categories',null=True,blank=True)
 
    def __unicode__(self):
        return ("%s"%(self.primary_name)) 
     
class PlaceCategory(models.Model):
    
    primary_category = models.ForeignKey(PrimaryCategory)
    is_paid = models.BooleanField(default=False)
    category_name = models.CharField(_("Category Name"), max_length=128,unique=True)
    description = models.TextField(_("Category Desc"),)
    is_active = models.BooleanField(_("Active Category"),default=True)
    image = models.ImageField(_("Image"),upload_to='categories',null=True,blank=True)

    def __unicode__(self):
        return "category_name:%s"%(self.category_name)

class PlaceDetail(models.Model):

    place_id = models.CharField(_("Place ID"), max_length=1024,unique=True,primary_key=True)
    place_name = models.CharField(_("Place Name"), max_length=128,blank=True)
    
    address = models.CharField(_("Address"), max_length=1024,blank=True,null=True)
    state = models.CharField(_("State"), max_length=64,blank=True)
    country = models.CharField(_("Country"), max_length=64,blank=True)
    postcode = models.CharField(_("Post Code"), max_length=30, blank=True)
        
    opening_hours = models.CharField(_("Opening Hours"), max_length=1024,blank=True,null=True)
    coordinates = models.PointField(_("Coordinates"),geography=True, srid=4326,blank=True,null=True)
    open_now = models.BooleanField(_("Open Now"),default=False)
    
    types = models.CharField(_("Place Types"), max_length=1024, blank=True,null=True)   #check it once again???????
    icon = models.CharField(_("Place Icon"), max_length=1024,blank=True,null=True)
    
    category = models.ForeignKey(PlaceCategory,null=True,blank=True)
    phone_number = models.CharField(_("Phone Number"), max_length=64,blank=True,null=True)
    web_link = models.CharField(_("Web Link"), max_length=1024,blank=True,null=True)
    place_tags = models.TextField(_("Place Tags"),blank=True)
    
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)

    class Meta:
        app_label = 'search'
        verbose_name = _('Place Search')
        verbose_name_plural = _('Places Search')
    
    objects = models.GeoManager()
    def __unicode__(self):
        return 'place_id:%s'%(self.place_id) 


class ReportError(models.Model):    
    
    place = models.ForeignKey(PlaceDetail,to_field='place_id',related_name='place_ref_error')
    error = models.TextField(_("Report Error"))
    
    address = models.BooleanField(_("Place Address"),default=False)
    opening_hours = models.BooleanField(_("Place Opening Hours"),default=False)
    phone_number = models.BooleanField(_("Place Phone Number"),default=False)
    
    date_added = models.DateTimeField(_("Date Added"), auto_now_add=True)
    last_modified = models.DateTimeField(_("Last Modified"), auto_now=True)
    
    def __unicode__(self):
        return "place_error:%s"%(self.place)

    
    
