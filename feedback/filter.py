from rest_framework import filters
from django.conf import settings
from django.db.models import Q
from search.models import PlaceDetail,PlaceCategory

class LocalFeedFilter(object):
    
    def get_query_param(self,request):
         
         query_param_dict={}
         point = request.query_params.get('point',None) 
         dist = int(request.query_params.get('distance',settings.DEFAULT_DISTANCE))
         category = request.query_params.get('category',None)   
         query_param_dict.update({'point':point,'dist':dist,'category':category})
         return query_param_dict
    
    def query_category_filter(self,request):
        place_model = PlaceDetail
        filter_param = self.get_query_param(request)
        category_name = [cat_name.strip() for cat_name in filter_param['category'].split(',')]
        cat_ids = PlaceCategory.objects.filter(category_name__in=category_name)
        ids = [obj.id for obj in cat_ids]
        queryset = (place_model.objects.filter(coordinates__dwithin=(filter_param['point'],filter_param['dist']))\
                                                                         .filter(category_id__in=ids)).values_list('place_id')                                                                 
        queryset_list = [place_id[0] for place_id in queryset]
        return queryset_list
         
class ReviewRatingLocalFeed(filters.BaseFilterBackend,LocalFeedFilter):
         
     def filter_queryset(self, request, queryset, view):
         
         filter_model = getattr(view,'model',None)
         filter_field = getattr(view,'point_filter_field',None)
         geoDjango_filter = 'dwithin'
         if request.query_params.get('category',None) :
             queryset_list = self.query_category_filter(request)
             return   filter_model.objects.filter(place_id__in=queryset_list)
         else:
             filter_param = self.get_query_param(request)
             return queryset.filter(Q(**{'%s__%s' % (filter_field, geoDjango_filter): (filter_param['point'], 
                                    filter_param['dist'])}))                  

class UploadImageLocalFeed(filters.BaseFilterBackend,LocalFeedFilter):
         
     def filter_queryset(self, request, queryset, view):
         
         filter_model = getattr(view,'model',None)
         filter_field = getattr(view,'point_filter_field',None)
         geoDjango_filter = 'dwithin'
         if request.query_params.get('category',None) :
             queryset_list = self.query_category_filter(request)
             return   filter_model.objects.filter(place_id__in=queryset_list)
         else:
             filter_param = self.get_query_param(request)
             return queryset.filter(Q(**{'%s__%s' % (filter_field, geoDjango_filter): (filter_param['point'], 
                                    filter_param['dist'])}))                  
             
             
             