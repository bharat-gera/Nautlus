from django.shortcuts import render
from rest_framework import generics
from feedback.models import ReviewRating,ReviewComment, ReviewLike,CommentLike,UploadImage,ImageLike,ImageComment,\
                     ImageCommentLike
from feedback.serializers import ReviewDetailSerializer,ReviewCommentSerializer,ReviewLikeSerializer,\
                CommentLikeSerializer, UploadImageSerializer,UploadImageLikeSerializer,UploadImageCommentSerializer,\
                UploadImageCommentLikeSerializer
from rest_framework import permissions
from django.http import JsonResponse,Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from permissions import OwnerPermission
from django.db.models import F
from rest_framework.views import APIView
from person.models import Person,ProfileImage

class ReviewDetailView(generics.ListCreateAPIView):
    
        
    serializer_class = ReviewDetailSerializer
    model = ReviewRating
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user).filter(is_deleted=False) 
    
    def perform_create(self, serializer):
        print serializer.data
        serializer.save(owner_id=self.request.user.id)

class ReviewShowDetail(generics.ListAPIView):
    """
    place_id -- place ID
    """

    serializer_class = ReviewDetailSerializer
    model = ReviewRating
    
    def get_query_params(self):
        if self.request.GET.get("place_id",None):
            return self.request.GET['place_id']
        raise Http404
    
    def get_queryset(self):
        return self.model.objects.filter(place_id=self.get_query_params()).filter(is_deleted=False) 
    
            
            
class ReviewEditView(OwnerPermission,generics.RetrieveUpdateDestroyAPIView):
    
    """
    pk is review_id
    """
    
    serializer_class = ReviewDetailSerializer
    model = ReviewRating
    permission_classes = (permissions.IsAuthenticated,OwnerPermission)
    
    def get_queryset(self):    
        return self.model.objects.filter(id=self.kwargs['pk']).filter(is_deleted=False)
    
    
    def delete(self, request,pk):
        instance = self.get_object()
        instance.is_deleted=True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewCommentView(generics.CreateAPIView):
    
    """
    pk is review_id
    
    """
    
    serializer_class = ReviewCommentSerializer
    model = ReviewComment
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,review_id=self.kwargs['pk'])     

class ReviewCommentEdit(generics.RetrieveUpdateDestroyAPIView,OwnerPermission):
    
    """
    id is comment_id
    
    """
    
    serializer_class = ReviewCommentSerializer
    model = ReviewComment
    permission_classes = (permissions.IsAuthenticated,OwnerPermission)
    lookup_field = 'id'
    
    def get_queryset(self):
        return self.model.objects.filter(owner_id=self.request.user).filter(id=self.kwargs['id']).filter(is_deleted=False)
    
    def delete(self, request,id):
        instance = self.get_object()
        ReviewRating.objects.filter(id=(instance.review_id)).update(comment_count = F('comment_count')-1)
        instance.is_deleted=True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ReviewLikeView(generics.ListCreateAPIView): 
       
    """
    pk is review_id
    """
    
    serializer_class = ReviewLikeSerializer
    model = ReviewLike
    permission_classes = (permissions.IsAuthenticated,)
    
    
    def get_queryset(self):
        return self.model.objects.filter(review_id=int(self.kwargs['pk']))
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,review_id=self.kwargs['pk'])  
        
class ReviewLikeEditView(OwnerPermission,generics.DestroyAPIView):   
    
    """
    pk is like_id
    
    """     
    
    serializer_class = ReviewLikeSerializer
    model = ReviewLike
    permission_classes = (permissions.IsAuthenticated,OwnerPermission)
    queryset = model.objects.all()
    
    def delete(self, request,pk):
        instance = self.get_object()
        ReviewRating.objects.filter(id=(instance.review_id)).update(like_count = F('like_count')-1)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CommentLikeView(generics.ListCreateAPIView):
    """
    id id comment_id
    
    """
    
    serializer_class = CommentLikeSerializer
    model = CommentLike
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'
    
    def get_queryset(self):
        return self.model.objects.filter(comment_id=int(self.kwargs['id']))
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,comment_id=int(self.kwargs['id']))  
 
class CommentLikeEditView(OwnerPermission,generics.DestroyAPIView):   
    
    """
    id is commnet_like_id
    
    """     
    
    serializer_class = CommentLikeSerializer
    model = CommentLike
    permission_classes = (permissions.IsAuthenticated,OwnerPermission)
    queryset = model.objects.all()
    lookup_field = 'id'
    
    def delete(self, request,id):
        instance = self.get_object()
        self.perform_destroy(instance)
        ReviewComment.objects.filter(id=int(instance.comment_id)).update(like_count = F('like_count')-1)
        return Response(status=status.HTTP_204_NO_CONTENT)
       
class UploadImageView(generics.ListCreateAPIView):
   
    serializer_class = UploadImageSerializer
    model = UploadImage
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user).filter(is_deleted=False)
    
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user) 

class UploadImageShow(generics.ListAPIView):
    """
   
    place_id -- Place ID
   
    """
    serializer_class = UploadImageSerializer
    model = UploadImage
    
    def get_query_params(self):
        if self.request.GET.get("place_id",None):
            return self.request.GET['place_id']
        raise Http404
    
    def get_queryset(self):
        return self.model.objects.filter(place_id=self.get_query_params()).filter(is_deleted=False)

class ReviewImagesDetail(generics.ListAPIView):
    
    serializer_class = UploadImageSerializer
    model = UploadImage
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user).filter(is_deleted=False)         
     
class UploadImageEdit(generics.DestroyAPIView,OwnerPermission):
    
    """
    pk is upload Image ID
    """
    
    serializer_class = UploadImageSerializer
    model = UploadImage
    permission_classes = (permissions.IsAuthenticated,OwnerPermission,)

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user,).filter(id=self.kwargs['pk'])
    
    def delete(self, request,pk):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UploadImageLikeView(generics.ListCreateAPIView):
    """
    pk is upload_image_like_id
    """
    
    
    serializer_class = UploadImageLikeSerializer
    model = ImageLike
    permission_classes = (permissions.IsAuthenticated,)
    
    
    def get_queryset(self):
        return self.model.objects.filter(upload_image_id=int(self.kwargs['pk']))
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,upload_image_id=int(self.kwargs['pk']))

class UploadImageLikeEdit(generics.DestroyAPIView,OwnerPermission):
    
    
    """
    pk is upload_image_like_id
    
    """     
    
    serializer_class = UploadImageLikeSerializer
    model = ImageLike
    permission_classes = (permissions.IsAuthenticated,OwnerPermission,)
    queryset = model.objects.all()
    
    def delete(self, request,pk):
        instance = self.get_object()
        UploadImage.objects.filter(id=(instance.upload_image_id)).update(like_count = F('like_count')-1)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
                   
class UploadImageComment(generics.CreateAPIView):
    
    """
    pk is image_id
    """
    
    serializer_class = UploadImageCommentSerializer
    model = ImageComment
    permission_classes = (permissions.IsAuthenticated,)    
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,upload_image_id=int(self.kwargs['pk']))

class UploadImageCommentEdit(generics.RetrieveUpdateDestroyAPIView,OwnerPermission):
    
    """
    pk is image_comment_id
    """
    
    
    serializer_class = ReviewCommentSerializer
    model = ImageComment
    permission_classes = (permissions.IsAuthenticated,OwnerPermission)
    
    def get_queryset(self):
        return self.model.objects.filter(owner_id=self.request.user).filter(id=self.kwargs['pk']).filter(is_deleted=False)
    
    def delete(self, request,pk):
        instance = self.get_object()
        UploadImage.objects.filter(id=int(instance.image_comment_id)).update(comment_count = F('comment_count')-1)
        instance.is_deleted=True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UploadImageCommentLike(generics.ListCreateAPIView): 
    
    """
    pk is image_comment_id
    """ 
    
    serializer_class = UploadImageCommentLikeSerializer
    model = ImageCommentLike
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return self.model.objects.filter(image_comment_id=int(self.kwargs['pk']))
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,image_comment_id=int(self.kwargs['pk']))  
 
class UploadImageCommentLikeEdit(OwnerPermission,generics.DestroyAPIView):   
    
    """
    pk is image_commnet_like_id
    
    """     
      
    serializer_class = UploadImageCommentLikeSerializer
    model = ImageCommentLike
    permission_classes = (permissions.IsAuthenticated,OwnerPermission)
    queryset = model.objects.all()
    
    def delete(self, request,pk):
        instance = self.get_object()
        self.perform_destroy(instance)
        ImageComment.objects.filter(id=int(instance.image_comment_id)).update(like_count = F('like_count')-1)
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
class TagFriendView(APIView): 
    
    """
    tag_name -- Name a friend 
    
    """   
    model = Person
    permission_classes =  (permissions.IsAuthenticated,)
    
    def get_query_params(self):
        if self.request.GET.get("tag_name",None):
            return self.request.GET['tag_name']
        raise Http404
    
    def get(self, request, format=None):
        search_name = {}
        user_obj = self.model.objects.filter(name__startswith=self.get_query_params())
        profile_obj = ProfileImage.objects.filter(owner__in=user_obj).values_list("image")
        search_name = {'suggestions':zip(user_obj.values_list('name'),profile_obj,user_obj.values_list('id'))}
        return Response(search_name,status=status.HTTP_200_OK)

class FeedbackCount(APIView):               
    """
    place_id -- place ID for extracting number of reviews and images
    """
    
    model = ReviewRating
    model_image = UploadImage
    
    def get_query_params(self):
        if self.request.GET.get("place_id",None):
            return self.request.GET['place_id']
        raise Http404
    
    def get(self,request,format=None):
        obj = self.model.objects.filter(place_id=self.get_query_params())
        obj_image = self.model_image.objects.filter(place_id=self.get_query_params())
        image_count = obj_image.count()
        review_count = obj.count()
        review_image_count = obj.count()
        total_rating_list = obj.values_list('rating')
        if total_rating_list:
            avg_rating = reduce(lambda x,y:x[0]+y[0],total_rating_list)/float(len(total_rating_list))
        else:
            avg_rating = None    
        data = {'statistics':{'review_count':review_count,'total_votes':review_count,'avg_rating':avg_rating,\
                              'total_images':image_count+review_image_count}}
        return Response(data,status=status.HTTP_200_OK)       

    
    
     