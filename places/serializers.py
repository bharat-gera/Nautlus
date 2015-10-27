from rest_framework import serializers
from places.models import Bookmarked,Beenhere,Favourites

class BookmarkedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bookmarked
        fields = ('id','is_marked',)
    
    def save(self,**kwargs):
        book_obj = Bookmarked.objects.filter(owner_id=kwargs['owner_id'],place_id=kwargs['place_id'])
        if not book_obj:
            return super(BookmarkedSerializer,self).save(**kwargs)
        raise serializers.ValidationError("Place is already Bookmarked")
            
class BeenhereSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Beenhere
        fields = ('id','is_here',)
        
    def save(self,**kwargs):
        book_obj = Beenhere.objects.filter(owner_id=kwargs['owner_id'],place_id=kwargs['place_id'])
        if not book_obj:
            return super(BeenhereSerializer,self).save(**kwargs)
        raise serializers.ValidationError("Place is already marked beenhere")
        
class FavouritesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Favourites
        fields = ('id','is_fav',)        
    
    def save(self,**kwargs):
        book_obj = Favourites.objects.filter(owner_id=kwargs['owner_id'],place_id=kwargs['place_id'])
        if not book_obj:
            return super(FavouritesSerializer,self).save(**kwargs)
        raise serializers.ValidationError("Place is already marked Favourite")
            