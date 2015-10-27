from uploadimages.models import UploadImage,ImageLike,ImageCommentLike,ImageComment
from rest_framework import serializers
from rest_framework_gis import serializers as gserializers
from feedback.permissions import start_tagging_friends
from django.db.models import F
from person.models import ProfileImage
from person.serializers import ProfileImageSerializer
    
class UploadImageLikeSerializer(serializers.ModelSerializer):        
    
    owner_name = serializers.CharField(source = 'owner.name', read_only=True)
    image_like = serializers.IntegerField(source = 'image.like_count',read_only=True)
    owner_image = serializers.SerializerMethodField()
    owner_id = serializers.SerializerMethodField()
    
    class Meta:
        model = ImageLike
        fields = ('id','owner_name','owner_image','owner_id','image_like',)
    
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
        UploadImage.objects.filter(id=validated_data['upload_image_id']).update(like_count = F('like_count')+1)
        return super(UploadImageLikeSerializer,self).save(**validated_data)


class UploadImageCommentLikeSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source = 'owner.name', read_only=True)
    like_image_comment = serializers.IntegerField(source = 'comment.like_count',read_only=True)
    owner_image = serializers.SerializerMethodField()
    owner_id = serializers.SerializerMethodField()
    
    class Meta:
        model = ImageCommentLike
        fields = ('id','owner_name','owner_image','owner_id','like_image_comment',) 
    
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
        ImageComment.objects.filter(id=int(validated_data['image_comment_id'])).update(like_count = F('like_count')+1)
        return super(UploadImageCommentLikeSerializer,self).save(**validated_data)     

class UploadImageCommentSerializer(serializers.ModelSerializer):
    
    owner_name = serializers.CharField(source = 'owner.name', read_only=True)
    owner_image = serializers.SerializerMethodField()
    image_comment = serializers.IntegerField(source = 'image.comment_count',read_only=True)
    like_image_comment = UploadImageCommentLikeSerializer(many=True, read_only=True)
    owner_id = serializers.SerializerMethodField()
    
    class Meta:
        model=ImageComment
        fields = ('id','comment','tag_friend','owner_name','owner_image','owner_id','image_comment','like_image_comment')
        
    def get_owner_id(self,obj):
        return obj.owner.id
    
    def get_owner_image(self,obj):
        obj = ProfileImage.objects.filter(owner_id=obj.owner.id)
        if not obj:
            return obj
        else:
            serializer = ProfileImageSerializer(obj[0])
            return serializer.data
    
    def save(self, **validated_data):
        if validated_data.get('tag_friend',None):
            tag_user_ids = validated_data.get('tag_friend').split(',')
            validated_data['tag_friend'] = start_tagging_friends(tag_user_ids)
        UploadImage.objects.filter(id=int(validated_data['upload_image_id'])).update(comment_count = F('comment_count')+1)
        return super(UploadImageCommentSerializer,self).save(**validated_data)         



class UploadImageSerializer(gserializers.GeoModelSerializer):
    
    like_image = UploadImageLikeSerializer(many=True,read_only=True)
    image_comment = UploadImageCommentSerializer(many=True,read_only=True)
    owner_name = serializers.CharField(source = 'owner.name', read_only=True)
    place_name = serializers.CharField(source='place.place_name',read_only=True)
    place_address = serializers.CharField(source='place.address',read_only=True)
    profile_image = serializers.SerializerMethodField()
    owner_id = serializers.SerializerMethodField()
    place_image = serializers.SerializerMethodField()
    
    class Meta:
        model = UploadImage
        fields = ('id','image','owner_name','place_name','place_address','profile_image','place_image',\
                  'owner_id','google_images','review_images','tag_friend','special_feature','with_whom',\
                  'location','like_image','image_comment','comment_count','like_count','review')
    
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
    
    def create(self, validated_data):
        print validated_data
        if validated_data.get('tag_friend',None):
            tag_user_ids = validated_data.get('tag_friend').split(',')
            validated_data['tag_friend'] = start_tagging_friends(tag_user_ids)
        if validated_data.get('with_whom',None):
            list_ids = validated_data.get('with_whom').split(',')
            validated_data['with_whom'] = start_tagging_friends(list_ids)
        return super(UploadImageSerializer,self).create(validated_data)     