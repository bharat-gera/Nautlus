from django.contrib import admin
from search.models import PrimaryCategory,PlaceCategory

class PrimaryCategoryAdmin(admin.ModelAdmin):
    
    list_display = ('primary_name','is_active','description','image',)
    actions = None
    
    def has_delete_permission(self,request,obj=None):
        return False
    
    
class PlaceCategoryAdmin(admin.ModelAdmin):
    
    list_display = ('category_name','is_paid','description','is_active','image','primary_category')
    actions = None
    
    
    def primary_category(self,obj):
    
        return obj.primary_category.primary_name
    
    def has_delete_permission(self,request,obj=None):
        return False

admin.site.register(PrimaryCategory,PrimaryCategoryAdmin)   
admin.site.register(PlaceCategory,PlaceCategoryAdmin)

 
