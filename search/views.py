from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from api_view import near_by_search,detail_search_place,auto_search_place,google_photo_search
from rest_framework.response import Response
from rest_framework import status
from events import SearchData,DetailSearchData
from search.serializers import PlaceCategorySerializer
from search.models import PlaceCategory
    
class SimpleSearch(APIView):
    """
    Simple search based on location and category,need either(loc and cat) or (cat and token)
    location -- coordinates of user's location (lat,long)
    category -- user's specific category search
    next_page_token -- next page token(pagination)
    radius -- distance for nearby search(max value:50000m)(unit in meters)
    """
    
    def filter_params(self,query_params):
        query_params_dict = {'category' : query_params.get('category',None),
                             'location' : query_params.get('location',None),
                             'next_page_token' : query_params.get('next_page_token',None),
                             'radius':query_params.get('radius',None)}
        return near_by_search(query_params_dict)
    
    def get(self, request):
        
        data = self.filter_params(self.request.query_params)
        q=SearchData()
        q.delay(ctx={'data':data,'category':self.request.query_params.get('category',None)})
        print data
        return Response(data,status=status.HTTP_200_OK)
    
class DetailSearchView(APIView):
    
    """
    Detail search based on place_id for a particular place
    place_id -- uniquely defines place details
    """
    
    def filter_params(self,query_params):
    
        query_params_dict = {'place_id':query_params.get('place_id',None)}
        return detail_search_place(query_params_dict)
    
    def get(self,request):
        
        data = self.filter_params(self.request.query_params)
        q=DetailSearchData()
        q.delay(ctx={'data':data,'place_id':self.request.query_params.get('place_id',None)})
        return Response(data,status=status.HTTP_200_OK)

class AutoCompleteSearchView(APIView):
    
    """
    Place AutoCompleteQuery on the specified parameters
    place_name -- name of a place
    location -- coordinates(lat,lng)
    """
    
    def filter_params(self,query_params):
    
        query_params_dict = {'place_name':query_params.get('place_name',None),
                             'location' : query_params.get('location',None)
                             }
        return auto_search_place(query_params_dict)
    
    def get(self,request):
        
        data = self.filter_params(self.request.query_params)
        return Response(data,status=status.HTTP_200_OK)

class ServiceCategoryView(generics.ListAPIView):
    
    """
    Service Category with pagination by 10
    page -- page query param
    """
    
    model = PlaceCategory
    serializer_class = PlaceCategorySerializer
    paginate_by = 2
    page_kwarg = 'page'

    def get_queryset(self):
        return PlaceCategory.objects.filter(is_active=True)

            
class GoogleImagesView(APIView):
    """
    Images for places

    photo_refr -- image reference ID
    maxheight -- max height for image in pixels(1-1600)
    maxwidth -- max width for image in pixels(1-1600)
    """
    
    
    def filter_params(self,query_params):
        
        query_params_dict = {'photo_refr':query_params.get('photo_refr',None),
                             'maxheight' : query_params.get('maxheight',None),
                             'maxwidth' : query_params.get('maxwidth',None),
                             }
        return google_photo_search(query_params_dict)
    
    def get(self,request):
        
        data = self.filter_params(self.request.query_params)
        return Response(data,status=status.HTTP_200_OK)             
        
        