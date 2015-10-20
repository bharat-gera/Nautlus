from rest_framework import serializers
from places.models import Bookmarked,Beenhere,Favourites

class BookmarkedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bookmarked
        fields = ('id','place_id',)
        

class BeenhereSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Beenhere
        fields = ('id','place_id',)
        
class FavouritesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Favourites
        fields = ('id','place_id',)        
        