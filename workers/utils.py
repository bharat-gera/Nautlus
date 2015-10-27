from celery import Task
import logging
from search.models import PlaceDetail,PlaceCategory
from uploadimages.models import UploadImage

logger = logging.getLogger('celery.task')

class CeleryTask(Task):

    events = 'simple_search','detail_search'
    
    def __call__(self,*args,**kwargs):
        logger.info("starting run to worker")
        return self.run(*args,**kwargs)
    
    def search_data_notifications(self,ctx):
        logger.info("search_data_entry_in_database")

        try:
            cat_obj = PlaceCategory.objects.get(category_name=ctx['category'])
        except PlaceCategory.DoesNotExist:
            logger.info("category doesn't exist")
        for param in ctx['data']['results']:
            if param.has_key('place_id') and ctx.get('category',None):
                obj,created = PlaceDetail.objects.get_or_create(place_id=param['place_id'],category_id=cat_obj.id)
            elif param.has_key('place_id'):
                obj,created = PlaceDetail.objects.get_or_create(place_id=param['place_id'])  
            if created:
                if 'opening_hours' in param:
                    obj.opening_hours = param.get('opening_hours',None)
                    obj.open_now = param.get('open_now',None)
                obj.place_name = param.get('name',None)
                obj.address = param.get('address',None)
                obj.coordinates = 'POINT('+str(param['coordinates']['lat'])+' '+str(param['coordinates']['lng']) + ')'
                obj.types = param.get('types',None)
                obj.icon = param.get('icon',None)
                obj.save()
                if 'photos' in param:
                    photo_obj,photo_created = UploadImage.objects.get_or_create(place_id=param['place_id'])
                    if photo_created:
                        photo_obj.location = 'POINT('+str(param['coordinates']['lat'])+' '+str(param['coordinates']['lng']) + ')'
                        logger.info('images_obj_created')
                        photo_obj.google_images = param.get('photos',None)
                        photo_obj.save()
                            
    def detail_search_data_notifications(self,ctx):
        
        logger.info("detail_search_data_notifications")
        
        try:
            update_values = {'place_id':ctx['data'].get('place_id',None),'place_name':ctx['data'].get('name',None),'address':ctx['data'].get('address',None),\
                            'coordinates':'POINT('+str(ctx['data']['coordinates']['lat'])+' '+str(ctx['data']['coordinates']['lng']) + ')',\
                            'types':ctx['data'].get('types',None),'icon':ctx['data'].get('icon',None),\
                            'phone_number':ctx['data'].get('phone_number',None),'web_link':ctx['data'].get('web_link',None)}
            
            obj,created = PlaceDetail.objects.update_or_create(place_id=ctx['place_id'],defaults=update_values)
            
            if 'opening_hours' in ctx['data'] and ctx['data']['opening_hours']!=None :
                obj.opening_hours = ctx['data'].get('opening_hours',None)
                obj.open_now = ctx['data'].get('open_now',None)
                obj.save()
            if ctx['data']['photos']!=None:
                for p_index in ctx['data']['photos']:
                    UploadImage(place_id=ctx['place_id'],google_images=ctx['data']['photos'],location=update_values['coordinates']).save()
        except PlaceDetail.DoesNotExist:
            logger.error("Place Detail doesn't exist")
     
            
    def perform_task(self,ctx):    

        if 'simple_search' in self.events:
            self.search_data_notifications(ctx)
        if 'detail_search'in self.events:
            self.detail_search_data_notifications(ctx)    
    
    def run(self, ctx):
        """The body of the task executed by workers."""
        logger.info("Run CeleryTask class")
        self.perform_task(ctx)
        
    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        logger.info("Ending run")
    