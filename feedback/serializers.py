from rest_framework import serializers
from feedback.models import ReviewRating,ReviewComment,ReviewLike,CommentLike
from rest_framework_gis import serializers as gserializers
from person.serializers import ProfileImageSerializer
from person.models import ProfileImage
from django.db.models import F
from permissions import start_tagging_friends,unpaid_review
from uploadimages.serializers import UploadImageSerializer 
from uploadimages.models import UploadImage
from django.shortcuts import get_object_or_404
from search.models import PlaceDetail,PlaceCategory
from django.conf import settings
import ast

class CommentLikeSerializer(serializers.ModelSerializer):
    
    owner_name = serializers.CharField(source = 'owner.name', read_only=True)
    like_comment = serializers.IntegerField(source = 'comment.like_count',read_only=True)
    owner_image = serializers.SerializerMethodField()
    owner_id = serializers.SerializerMethodField()
    
    class Meta:
        model = CommentLike
        fields = ('id','owner_name','like_comment','owner_image','owner_id',) 
    
    def get_owner_image(self,obj):
        obj = ProfileImage.objects.filter(owner_id=obj.owner.id)
        if not obj:
            return obj
        else:
            serializer = ProfileImageSerializer(obj[0])
            return serializer.data
        
    def get_owner_id(self,obj):
        return obj.owner.id
        
    def save(self, **validated_data):
        ReviewComment.objects.filter(id=int(validated_data['comment_id'])).update(like_count = F('like_count')+1)
        return super(CommentLikeSerializer,self).save(**validated_data)    

class ReviewCommentSerializer(serializers.ModelSerializer):
    
    owner_name = serializers.CharField(source = 'owner.name', read_only=True)
    owner_image = serializers.SerializerMethodField()
    review_comment = serializers.IntegerField(source = 'review.comment_count',read_only=True)
    like_comment = CommentLikeSerializer(many=True, read_only=True)
    owner_id = serializers.SerializerMethodField()
    
    class Meta:
        model = ReviewComment
        fields=('id','comment','tag_friend','owner_name','owner_image','owner_id','like_comment','review_comment') 
    
    def get_owner_id(self,obj):
        return obj.owner.id
        
    def save(self, **validated_data):
        
        if validated_data.get('tag_friend',None):
            tag_user_ids = validated_data.get('tag_friend').split(',')
            validated_data['tag_friend'] = start_tagging_friends(tag_user_ids)
        ReviewRating.objects.filter(id=int(validated_data['review_id'])).update(comment_count = F('comment_count')+1)
        return super(ReviewCommentSerializer,self).save(**validated_data)
        
    def get_owner_image(self,obj):

        obj = ProfileImage.objects.filter(owner_id=obj.owner.id)
        if not obj:
            return obj
        else:
            serializer = ProfileImageSerializer(obj[0])
            return serializer.data

class ReviewLikeSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source = 'owner.name', read_only=True)
    review_like = serializers.IntegerField(source = 'review.like_count',read_only=True)
    owner_image = serializers.SerializerMethodField()
    owner_id = serializers.SerializerMethodField()
   
    class Meta:
        model = ReviewLike 
        fields = ('id','owner_name','owner_image','owner_id','review_like',)
    
    def get_owner_image(self,obj):
        obj = ProfileImage.objects.filter(owner_id=obj.owner.id)
        if not obj:
            return obj
        else:
            serializer = ProfileImageSerializer(obj[0])
            return serializer.data
    def get_owner_id(self,obj):
        return obj.owner.id
    
    def save(self, **validated_data):
        ReviewRating.objects.filter(id=validated_data['review_id']).update(like_count = F('like_count')+1)
        return super(ReviewLikeSerializer,self).save(**validated_data)    
    
      
class ReviewDetailSerializer(gserializers.GeoModelSerializer):
    
    comment = ReviewCommentSerializer(many=True, read_only=True)
    like_review = ReviewLikeSerializer(many=True, read_only=True)
    images_review = UploadImageSerializer(read_only=True,source='uploadimage_set',many=True)
    owner_name = serializers.CharField(source = 'owner.name', read_only=True)
    place_name = serializers.CharField(source='place.place_name',read_only=True)
    place_address = serializers.CharField(source='place.address',read_only=True)
    profile_image = serializers.SerializerMethodField()
    owner_id = serializers.SerializerMethodField()
    place_image = serializers.SerializerMethodField()
    
    class Meta:
        model = ReviewRating
        fields = ('id','owner_name','profile_image','place_name','place_image','owner_id','place_address','review_detail',\
                  'rating','with_whom','tag_friend','location',\
                  'comment_count','like_count','comment','like_review','images_review')
    
    def get_place_image(self,obj):
        obj = UploadImage.objects.filter(place_id=obj.place_id).values_list('google_images')
        return obj
        
    def get_owner_id(self,obj):
        return obj.owner.id
    
    def get_profile_image(self,obj):
        obj = ProfileImage.objects.filter(owner_id=obj.owner.id)
        if not obj:
            return obj
        else:
            serializer = ProfileImageSerializer(obj[0])
            return serializer.data
    
    def validate_review_detail(self,value):
        num_chars = len(value.replace(' ',''))
        if num_chars < settings.MIN_REVIEW_LENGTH:
            raise serializers.ValidationError("Minimum Required Length for Review:120characters.")        
        return value
    
    def create(self, validated_data):
        
        review_obj = ReviewRating.objects.filter(place_id=validated_data['place_id']).filter(owner=validated_data['owner'])
        if review_obj:
            raise serializers.ValidationError("You have already reviewed this place.") 
        
        place_obj = get_object_or_404(PlaceDetail,place_id=validated_data['place_id'])
        if validated_data['location'] == place_obj.coordinates:
            if validated_data.get('tag_friend',None):
                tag_user_ids = validated_data.get('tag_friend').split(',')
                validated_data['tag_friend'] = start_tagging_friends(tag_user_ids)
            if validated_data.get('with_whom',None):
                list_ids = validated_data.get('with_whom').split(',')
                validated_data['with_whom'] = start_tagging_friends(list_ids)
            obj = super(ReviewDetailSerializer,self).create(validated_data)
            cat_list = PlaceCategory.objects.filter(category_name__in=ast.literal_eval(place_obj.types)).\
                                                    values_list('is_paid',flat=True)
            if not True in cat_list:
                unpaid_review(obj)  
            return obj                                                
        else:
            raise serializers.ValidationError("User's location is different from place")
            
        