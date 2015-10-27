from rest_framework import generics
from places.models import Bookmarked,Beenhere,Favourites
from places.serializers import BookmarkedSerializer,BeenhereSerializer,FavouritesSerializer
from rest_framework import permissions
from feedback.permissions import OwnerPermission
from rest_framework.response import Response
from rest_framework import status

class BookmarkedListView(generics.ListAPIView):
    
    """
    place_id -- place_id
    """
    
    model = Bookmarked
    serializer_class = BookmarkedSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        if self.request.GET.get('place_id',None):
            return self.model.objects.filter(owner=self.request.user).filter(place_id=self.request.GET['place_id'])
        else:
            return self.model.objects.filter(owner=self.request.user)

class BookmarkedView(generics.CreateAPIView):
    
    """
    Mark Place as BookMarked
    """
    
    model = Bookmarked
    serializer_class = BookmarkedSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'place_id'
    
    def perform_create(self,serializer):
        return serializer.save(owner_id=self.request.user.id,place_id=self.kwargs['place_id'])
    
class BookmarkedEditView(generics.DestroyAPIView,OwnerPermission):
    
    """
       pk is Bookmarked ID
    """
    
    model = Bookmarked
    serializer_class = BookmarkedSerializer
    permission_classes = (permissions.IsAuthenticated,OwnerPermission,)
    
    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)
    
    def delete(self,request,pk):
        instance = self.get_object()
        print instance
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class BeenHereListView(generics.ListAPIView):
    
    """
    place_id -- place_id
    """
    
    model = Beenhere
    serializer_class = BeenhereSerializer
    permission_classes = (permissions.IsAuthenticated,)
     
    def get_queryset(self):
        if self.request.GET.get('place_id',None):
            return self.model.objects.filter(owner=self.request.user).filter(place_id=self.request.GET['place_id'])
        else:
            return self.model.objects.filter(owner=self.request.user)


class BeenHereView(generics.CreateAPIView):
    
    """
    Mark Place as Beenhere
    """
    
    model = Beenhere
    serializer_class = BeenhereSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'place_id'
    
    
    def perform_create(self,serializer):
        return serializer.save(owner_id=self.request.user.id,place_id=self.kwargs['place_id'])

class BeenhereEditView(generics.DestroyAPIView,OwnerPermission):

    """
       pk is Beenhere ID
    """
    
    model = Beenhere
    serializer_class = BeenhereSerializer
    permission_classes = (permissions.IsAuthenticated,OwnerPermission,)
    
    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)
    
    def delete(self,request,pk):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class FavouriteListView(generics.ListAPIView):
    
    """
    place_id -- place_id
    """

    model = Favourites
    serializer_class = FavouritesSerializer
    permission_classes = (permissions.IsAuthenticated,)
     
    def get_queryset(self):
        if self.request.GET.get('place_id',None):
            return self.model.objects.filter(owner=self.request.user).filter(place_id=self.request.GET['place_id'])
        else:
            return self.model.objects.filter(owner=self.request.user)

class FavouriteView(generics.CreateAPIView):
    
    """
    Mark place as favourite
    """
    
    model = Favourites
    serializer_class = FavouritesSerializer
    permission_classes = (permissions.IsAuthenticated,)
   
    
    def perform_create(self,serializer):
        return serializer.save(owner_id=self.request.user.id,place_id=self.kwargs['place_id'])
    
class FavouriteEditView(generics.DestroyAPIView,OwnerPermission):
    
    """
       pk is Favourite ID
    """
    
    model = Favourites
    serializer_class = FavouritesSerializer
    permission_classes = (permissions.IsAuthenticated,OwnerPermission,)
    
    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)
    
    def delete(self,request,pk):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    
        
        
        
    
    
