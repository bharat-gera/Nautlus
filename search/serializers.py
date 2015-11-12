from rest_framework import serializers
from search.models import PlaceCategory,PrimaryCategory

class PlaceCategorySerializer(serializers.ModelSerializer):
    
    primary_cat = serializers.CharField(source='primary_category.primary_name',read_only=True)
    
    class Meta:
        model = PlaceCategory
        fields = ('id','category_name','description','image','is_active','primary_cat',)

class PrimaryCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PrimaryCategory
        fields = ('id','primary_name','description','is_active','image',)    