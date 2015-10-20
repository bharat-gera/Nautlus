from rest_framework import serializers
from feedback.models import ReviewRating,ReviewComment,ReviewLike,CommentLike,UploadImage,ImageLike,\
                             ImageComment,ImageCommentLike
from rest_framework_gis import serializers as gserializers
from person.serializers import ProfileImageSerializer
from person.models import ProfileImage
from django.db.models import F
from permissions import start_tagging_friends

class CommentLikeSerializer(serializers.ModelSerializer):
    
    owner_name = serializers.CharField(source = 'owner.name', read_only=True)
    like_comment = serializers.IntegerField(source = 'comment.like_count',read_only=True)
    
    class Meta:
        model = CommentLike
        fields = ('id','owner_name','like_comment',) 
        
    def create(self, validated_data):
        super(CommentLikeSerializer,self).create(validated_data)
        ReviewComment.objects.filter(id=int(validated_data['comment_id'])).update(like_count = F('like_count')+1)
        return CommentLike(**validated_data)    

class ReviewCommentSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source = 'owner.name', read_only=True)
    #image = serializers.SerializerMethodField()
    review_comment = serializers.IntegerField(source = 'review.comment_count',read_only=True)
    like_comment = CommentLikeSerializer(many=True, read_only=True)
    class Meta:
        model = ReviewComment
        fields=('id','comment','tag_friend','owner_name','like_comment','review_comment') 
        
    def create(self, validated_data):
        
        if validated_data.get('tag_friend',None):
            tag_user_ids = validated_data.get('tag_friend').split(',')
            validated_data['tag_friend'] = start_tagging_friends(tag_user_ids)
        super(ReviewCommentSerializer,self).create(validated_data)
        ReviewRating.objects.filter(id=int(validated_data['review_id'])).update(comment_count = F('comment_count')+1)
        return ReviewComment(**validated_data)
        
'''        
        def get_image(self,obj):
            obj = ProfileImage.objects.filter(owner_id=obj.owner.id)
            if not obj:
                return obj
            else:
                serializer = ProfileImageSerializer(obj[0])
                return serializer.data
'''
class ReviewLikeSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source = 'owner.name', read_only=True)
    review_like = serializers.IntegerField(source = 'review.like_count',read_only=True)
    
    class Meta:
        model = ReviewLike 
        fields = ('id','owner_name','review_like',)
    
    def create(self, validated_data):
        ReviewRating.objects.filter(id=validated_data['review_id']).update(like_count = F('like_count')+1)
        super(ReviewLikeSerializer,self).create(validated_data)
        return ReviewLike(**validated_data)    
    
class ReviewDetailSerializer(gserializers.GeoModelSerializer):
    
    comment = ReviewCommentSerializer(many=True, read_only=True)
    like_review = ReviewLikeSerializer(many=True, read_only=True)
    
    class Meta:
        model = ReviewRating
        fields = ('id','review_detail','rating','with_whom','tag_friend','place_id','location',
                  'comment_count','like_count','comment','like_review',)
    
    def create(self, validated_data):
        print validated_data
        if validated_data.get('tag_friend',None):
            tag_user_ids = validated_data.get('tag_friend').split(',')
            validated_data['tag_friend'] = start_tagging_friends(tag_user_ids)
        if validated_data.get('with_whom',None):
            list_ids = validated_data.get('with_whom').split(',')
            validated_data['with_whom'] = start_tagging_friends(list_ids)
        return super(ReviewDetailSerializer,self).create(validated_data)   
                                                                   
  
    
class UploadImageLikeSerializer(serializers.ModelSerializer):        
    
    owner_name = serializers.CharField(source = 'owner.name', read_only=True)
    image_like = serializers.IntegerField(source = 'image.like_count',read_only=True)
    class Meta:
        model = ImageLike
        fields = ('id','owner_name','image_like',)
    
    def create(self, validated_data):
        UploadImage.objects.filter(id=validated_data['upload_image_id']).update(like_count = F('like_count')+1)
        super(UploadImageLikeSerializer,self).create(validated_data)
        return ImageLike(**validated_data)  


class UploadImageCommentLikeSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source = 'owner.name', read_only=True)
    like_image_comment = serializers.IntegerField(source = 'comment.like_count',read_only=True)
    
    class Meta:
        model = ImageCommentLike
        fields = ('id','owner_name','like_image_comment',) 
        
    def create(self, validated_data):
        super(UploadImageCommentLikeSerializer,self).create(validated_data)
        ImageComment.objects.filter(id=int(validated_data['image_comment_id'])).update(like_count = F('like_count')+1)
        return ImageCommentLike(**validated_data)     

class UploadImageCommentSerializer(serializers.ModelSerializer):
    
    owner_name = serializers.CharField(source = 'owner.name', read_only=True)
    #image = serializers.SerializerMethodField()
    image_comment = serializers.IntegerField(source = 'image.comment_count',read_only=True)
    like_comment = UploadImageCommentLikeSerializer(many=True, read_only=True)
    
    class Meta:
        model=ImageComment
        fields = ('id','comment','tag_friend','owner_name','image_comment','like_comment')
        
    def create(self, validated_data):
        if validated_data.get('tag_friend',None):
            tag_user_ids = validated_data.get('tag_friend').split(',')
            validated_data['tag_friend'] = start_tagging_friends(tag_user_ids)
        super(UploadImageCommentSerializer,self).create(validated_data)
        UploadImage.objects.filter(id=int(validated_data['upload_image_id'])).update(comment_count = F('comment_count')+1)
        return ImageComment(**validated_data)         
    
class UploadImageSerializer(serializers.ModelSerializer):
    
    like_image = UploadImageLikeSerializer(many=True,read_only=True)
    image_comment = UploadImageCommentSerializer(many=True,read_only=True)
    class Meta:
        model = UploadImage
        fields = ('id','place_id','image','google_images','tag_friend','special_feature','with_whom','location','like_image','image_comment',
                  'comment_count','like_count')

    def create(self, validated_data):

        if validated_data.get('tag_friend',None):
            tag_user_ids = validated_data.get('tag_friend').split(',')
            validated_data['tag_friend'] = start_tagging_friends(tag_user_ids)
        if validated_data.get('with_whom',None):
            list_ids = validated_data.get('with_whom').split(',')
            validated_data['with_whom'] = start_tagging_friends(list_ids)
        return super(ReviewDetailSerializer,self).create(validated_data)                                                              
      
    
    
    
    
            
            
        