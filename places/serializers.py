from rest_framework import serializers
from places.models import Bookmarked,Beenhere,Favourites,FollowFriends
from person.models import ProfileImage,Person
from person.serializers import ProfileImageSerializer

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

class FollowFriendsSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()
    
    class Meta:
        model = FollowFriends
        fields = ('following','follower','profile_image','name',)
        read_only_fields = ('follower','profile_image','name',)
    
    def get_name(self,obj):
        
        if self.context['request'].GET['param'] == 'following':
            obj = Person.objects.get(id=obj.following.id)
            return obj.name
        elif self.context['request'].GET['param'] == 'follower':
            obj = Person.objects.get(id=obj.follower.id)
            return obj.name
        
    def get_profile_image(self,obj):
        
        if self.context['request'].GET['param'] == 'following':
            obj = ProfileImage.objects.filter(owner_id=obj.following.id)
        elif self.context['request'].GET['param'] == 'follower':
            obj = ProfileImage.objects.filter(owner_id=obj.follower.id)
        serializer = ProfileImageSerializer(obj[0])
        return serializer.data
    
    def validate(self,data):
        if FollowFriends.objects.filter(follower_id=self.context['request'].user.id,following_id=data['following'].id).count():
            raise serializers.ValidationError("Already following this friend")
        return data    
            