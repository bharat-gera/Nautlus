from django.shortcuts import render
from feedback.models import ReviewRating
from uploadimages.models import UploadImage
from feedback.serializers import ReviewDetailSerializer
from uploadimages.serializers import UploadImageSerializer
from django.http import JsonResponse,Http404
from rest_framework.response import Response
from rest_framework import status
from feedback.permissions import OwnerPermission
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import generics
from feedback.filter import ReviewRatingLocalFeed,UploadImageLocalFeed 
from person.models import Person,ProfileImage

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

class LocalFeedReview(generics.ListAPIView):
    
    """
     LocalFeed For Review Rating,default distance=50km(inner circle)
     point -- user's location
     category -- feed category
     distance -- distance for local feed
    """
    
    model = ReviewRating
    serializer_class = ReviewDetailSerializer
    filter_backends = (ReviewRatingLocalFeed,)
    point_filter_field = 'location'
    queryset = model.objects.all()
    
class LocalFeedImages(generics.ListAPIView):
    
    """
     LocalFeed For Images,default distance=50km(inner circle)
     point -- user's location
     category -- feed category
     distance -- distance for local feed
    """
    
    model = UploadImage
    serializer_class = UploadImageSerializer
    filter_backends = (UploadImageLocalFeed,)
    point_filter_field = 'location'
    queryset = model.objects.all()
    
    
    