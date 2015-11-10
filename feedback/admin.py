from django.contrib import admin
from feedback.models import ReviewRating
from django.forms.widgets import Textarea
from django.contrib.gis.db import models
from feedback.utils import BusinessRating

class ReviewRatingAdmin(admin.ModelAdmin):
    
    model = ReviewRating
    date_hierarchy = 'date_added'
    list_display = ('id','review_detail','owner','place_detail','rating','location','is_verified','is_credited','is_deleted',
              'comment_count','like_count','date_added','last_modified',)
    readonly_fields = ('date_added','last_modified','review_detail','owner','place_detail','rating','place','is_verified',
                       'is_credited','comment_count','like_count','location')
    #search_fields = ('id','review_detail','owner__email','location','is_credited','place_detail')
    #list_filter = ('date_added','last_modified',)
    actions = ['verified_review']
    exclude = ('with_whom','tag_friend',)
    formfield_overrides = {
        models.PointField: {'widget': Textarea }
    }
    
    def place_detail(self,obj):
        return "Name:%s,Address:%s"%(obj.place.place_name,obj.place.address)
    
    def verified_review(self,request,queryset):
        
        for obj in queryset:    
            if not obj.is_verified:
                obj.is_verified=True
                obj.save()
                BusinessRating().user_wallet(obj)
                self.message_user(request,"Review for place_id:%s from user_email:%s marked as verified"%(obj.place_id,obj.owner.email))
            else:
                self.message_user(request,"Review with id:%s is already marked verified and credited"%(obj.id))                    
    verified_review.short_description = 'Mark Review Verified'
   
    
    def get_actions(self,request):
        actions = super(ReviewRatingAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions   
    
    def has_delete_permission(self,request,obj=None):
        return False
    def has_add_permission(self, request):
        return False
       
admin.site.register(ReviewRating,ReviewRatingAdmin)    


