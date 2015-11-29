from django.conf import settings
import requests
from django.http import JsonResponse
from feedback.models import ReviewRating
from uploadimages.models import UploadImage

def simple_search_parser(req_json):
    json_list = []
    json_dict,final_dict={},{}
    for param in req_json['results']:
        json_dict = {'name':param.get('name',None),'place_id':param.get('place_id',None),'address':param.get('vicinity',None), \
                            'coordinates':param['geometry']['location'],'types':param.get('types',None),\
                            'icon':param.get('icon',None)}
        if 'opening_hours' in param: 
            json_dict.update({'opening_hours':param['opening_hours']['weekday_text']})
            json_dict.update({'open_now' :param['opening_hours']['open_now']})
        if 'photos' in param:          
            json_dict.update({'photos': param['photos']})
        json_dict.update({'statistics':feedback_count(param.get('place_id',None))})    
        json_list.append(json_dict)
    final_dict.update({'results':json_list})
    if req_json.has_key('next_page_token'):
        final_dict.update({'page_token':req_json['next_page_token']})
    return final_dict
    
def near_by_search(query_params):
    
    if (not query_params['next_page_token']) and (query_params['location'] and query_params['category']):
        query = settings.GOOGLE_NEAR_BY + 'location='+query_params['location']+'&rankby=distance'+'&types=' + \
                                                           query_params['category'] + '&key=' + settings.GOOGLE_API_KEY
    elif query_params['next_page_token']:
        query = settings.GOOGLE_NEAR_BY + 'pagetoken=' +query_params['next_page_token'] + '&key=' + settings.GOOGLE_API_KEY   
    elif query_params['radius'] and query_params['location']:
        query = settings.GOOGLE_NEAR_BY + 'location='+query_params['location']+'&radius='+query_params['radius'] \
                                                            + '&key=' + settings.GOOGLE_API_KEY
    else:
        response = JsonResponse({'Error': 'Searching either based on (category and location) or (token and category)'})
        return response.content
    
    req = requests.get(query)
    return simple_search_parser(req.json())

def detail_search_parser(req_json):
    
    result = req_json['result']
    if result:
        json_dict = {'web_link':result.get('website',None),'name':result.get('name',None),'photos':result.get('photos',None), \
                            'coordinates':result['geometry'].get('location',None),'place_id':result.get('place_id',None),\
                            'address':result.get('formatted_address',None),'phone_number':result.get('international_phone_number',None),\
                            'periods':result.get('periods',None),'types':result.get('types',None),'icon':result.get('icon',None)}
        if 'opening_hours' in result: 
            json_dict.update({'opening_hours':result['opening_hours']['weekday_text']})
            json_dict.update({'open_now' :result['opening_hours']['open_now']})
        json_dict.update({'statistics':feedback_count(result.get('place_id',None))})    
    
        return json_dict
    else:     
        response = JsonResponse({'Error': 'No result found'})
        return response.content

def detail_search_place(query_params):
    
    if query_params['place_id']:
        query = settings.GOOGLE_DETAIL_API + 'placeid='+query_params['place_id']+'&key=' + settings.GOOGLE_API_KEY
    else:
        response = JsonResponse({'Error': 'Detail Searching  based on place_id'})
        return response.content
    req=requests.get(query)
    return detail_search_parser(req.json())   

def auto_search_parser(req_json):
    results = req_json.get('predictions',None)
    json_list=[]
    final_dict = {}
    if results:
        for param in results:
            json_dict = {'description':param.get('description',None),'place_id':param.get('place_id',None)}
            json_list.append(json_dict)
        final_dict.update({'results':json_list})
        return final_dict
    else:     
        response = JsonResponse({'Error': 'No result found'})
        return response.content
def auto_search_place(query_params):
    
    if query_params['place_name'] and query_params['location']:
        query = settings.GOOGLE_AUTO_API + 'input=' + query_params['place_name'] + '&location='+ query_params['location'] +\
                                                                      '&radius=' + str(settings.NEAR_BY_RADIUS) + '&key='+settings.GOOGLE_API_KEY 
                                                                                                   
    else:
        response = JsonResponse({'Error': 'Input is invalid'})
        return response.content
    req=requests.get(query)
    return auto_search_parser(req.json())

def google_photo_search(query_params):
    
    if query_params['photo_refr'] and query_params['maxheight'] and query_params['maxwidth']:
        query = settings.GOOGLE_PHOTO_API + 'photoreference='+query_params['photo_refr']+ '&maxheight='+query_params['maxheight']+\
                                                                                 '&maxwidth='+query_params['maxwidth']+\
                                                                                 '&key='+settings.GOOGLE_API_KEY
    else:
        response = JsonResponse({'Error': 'Image not available'})
        return response.content                                                                             
    req=requests.get(query)
    return req.json()


def formated_list(list_input):
    image_list = [x for x in list(list_input) if x.strip()]
    if image_list:
        return len(image_list)
    else:
        return 0 
def feedback_count(place_id):
    
    model = ReviewRating
    model_image = UploadImage

    obj = model.objects.filter(place_id=place_id)
    obj_image = model_image.objects.filter(place_id=place_id)
    image_count = formated_list(obj_image.values_list('image',flat=True)) 
    google_image = formated_list(obj_image.values_list('google_images',flat=True))
    review_images = formated_list(obj_image.values_list('review_images',flat=True))
    review_count = obj.count()
    review_image_count = obj.count()
    total_rating_list = obj.values_list('rating')
    if total_rating_list:
        avg_rating = reduce(lambda x,y:x+y,[num[0] for num in total_rating_list])/len(total_rating_list)
    else:
        avg_rating = None    
    data = {'review_count':review_count,'total_votes':review_count,'avg_rating':avg_rating,\
                              'total_uploaded_images':{'image_count':image_count,'google_image':google_image,\
                                                       'review_images':review_images}}

    return data


