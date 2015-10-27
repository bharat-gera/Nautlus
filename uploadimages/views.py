from uploadimages.models import UploadImage,ImageComment,ImageLike,ImageCommentLike
from uploadimages.serializers import UploadImageSerializer,UploadImageLikeSerializer,\
                                              UploadImageCommentLikeSerializer,UploadImageCommentSerializer
from rest_framework import permissions
from rest_framework import generics
from feedback.permissions import OwnerPermission
from django.http import Http404

class UploadImageView(generics.CreateAPIView):
   
    serializer_class = UploadImageSerializer
    model = UploadImage
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'place_id'
    
    
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user,place_id=self.kwargs['place_id']) 

class UploadImageShow(generics.ListAPIView):
    """
   
    place_id -- Place ID
   
    """
    serializer_class = UploadImageSerializer
    model = UploadImage
    
    def get_query_params(self):
        return self.request.GET['place_id']
    
    def get_queryset(self):
        if self.request.GET.get('place_id',None):
            return self.model.objects.filter(place_id=self.get_query_params()).filter(is_deleted=False)
        elif self.request.user.is_authenticated():
            return self.model.objects.filter(owner_id=self.request.user.id).filter(is_deleted=False)
        
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
    see_all -- True for seeing all reviews,False for user specific
    """
    
    
    serializer_class = UploadImageLikeSerializer
    model = ImageLike
    permission_classes = (permissions.IsAuthenticated,)
    
    
    def get_queryset(self):
        if str(self.request.GET['see_all']).lower()=='false':
            self.model.objects.filter(upload_image_id=int(self.kwargs['pk'])).filter(owner_id=self.request.user.id)
        else:    
            return self.model.objects.filter(upload_image_id=int(self.kwargs['pk']))
    
    def perform_create(self, serializer):
        obj = self.model.objects.filter(owner=self.request.user).filter(upload_image_id=self.kwargs['pk']).count()
        if obj:
            raise Http404
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
                   
class UploadImageComment(generics.ListCreateAPIView):
    
    """
    pk is image_id
    """
    
    serializer_class = UploadImageCommentSerializer
    model = ImageComment
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)    
    
    def get_queryset(self):
        return self.model.objects.filter(upload_image_id=self.kwargs['pk'])
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,upload_image_id=int(self.kwargs['pk']))

class UploadImageCommentEdit(generics.RetrieveUpdateDestroyAPIView,OwnerPermission):
    
    """
    pk is image_comment_id
    """
    
    
    serializer_class = UploadImageCommentSerializer
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
        obj = self.model.objects.filter(owner=self.request.user).filter(image_comment_id=self.kwargs['pk']).count()
        if obj:
            raise Http404
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

