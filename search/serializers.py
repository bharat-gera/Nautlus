from rest_framework import serializers
from search.models import PlaceCategory

class PlaceCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlaceCategory
        fields = ('id','category_name','description','image','is_active')

#class SimpleSearchSerializer(serializers.Serializer):
    
    