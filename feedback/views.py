from django.shortcuts import render
from rest_framework import generics
from feedback.models import ReviewRating,ReviewComment, ReviewLike,CommentLike
from feedback.serializers import ReviewDetailSerializer,ReviewCommentSerializer,ReviewLikeSerializer,\
                CommentLikeSerializer
from rest_framework import permissions
from django.http import JsonResponse,Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from permissions import OwnerPermission
from django.db.models import F
from rest_framework.views import APIView
from person.models import Person,ProfileImage
from filter import ReviewRatingLocalFeed

class ReviewDetailView(generics.CreateAPIView):
    
        
    serializer_class = ReviewDetailSerializer
    model = ReviewRating
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'place_id'
     
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,place_id=self.kwargs['place_id'])

class ReviewShowDetail(generics.ListAPIView):
    """
    place_id -- place ID
    """

    serializer_class = ReviewDetailSerializer
    model = ReviewRating
    
    def get_query_params(self):
        
        return self.request.GET['place_id']
    
    def get_queryset(self):

        if  self.request.GET.get("place_id",None):
            return self.model.objects.filter(place_id=self.get_query_params()).\
                                             filter(is_deleted=False).filter(is_verified=True) 
        elif self.request.user.is_authenticated():
            return self.model.objects.filter(owner=self.request.user).\
                                            filter(is_deleted=False).filter(is_verified=True)
    
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

class ReviewCommentView(generics.ListCreateAPIView):
    
    """
    pk is review_id
    
    """
    
    serializer_class = ReviewCommentSerializer
    model = ReviewComment
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get_queryset(self):
        return self.model.objects.filter(review_id=self.kwargs['pk'])
        
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
    see_all -- True for seeing all reviews,False for user specific
    """
    
    serializer_class = ReviewLikeSerializer
    model = ReviewLike
    permission_classes = (permissions.IsAuthenticated,)
    
    
    def get_queryset(self):
        
        if str(self.request.GET['see_all']).lower()=='false':
            self.model.objects.filter(review_id=int(self.kwargs['pk'])).filter(owner_id=self.request.user.id)
        return self.model.objects.filter(review_id=int(self.kwargs['pk']))
    
    def perform_create(self, serializer):
        
        obj = self.model.objects.filter(owner=self.request.user).filter(review_id=self.kwargs['pk']).count()
        if obj:
            raise Http404
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
        obj = self.model.objects.filter(owner=self.request.user).filter(comment_id=self.kwargs['id']).count()
        if obj:
            raise Http404
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
       
     