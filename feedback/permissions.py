from rest_framework import permissions
import json
from django.conf import settings
class OwnerPermission(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        return obj.owner == request.user
    
    
def start_tagging_friends(tag_user_ids):
    tag_list = []
    for ids in tag_user_ids:
        profile_url = settings.PROFILE_URL + '/' +str(ids)
        tag_friend_ids = {'owner_id':ids,'profile_url':profile_url}
        tag_list.append(tag_friend_ids)
    return json.dumps(tag_list)         