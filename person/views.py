from person.models import Profile,Person,ProfileImage
from rest_framework import generics,permissions,status
from rest_framework.response import Response
from person.serializers import ProfileSerializer,PersonSerializer,ProfileImageSerializer
from django.shortcuts import get_object_or_404
# Create your views here.
class ProfileView(generics.RetrieveUpdateAPIView):
    """
        Profile view
        owner_id -- owner ID for profile View
    """
    model = Profile
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        if request.GET.get('owner_id',None):
            person = Person.objects.get(pk=request.GET['owner_id'])
        else:    
            person = get_object_or_404(Person,pk=request.user.id)
        serializer = PersonSerializer(person)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        profile = self.model.objects.get(owner=request.user)
        person = Person.objects.get(pk=request.user.id)

        name = request.data.get('name',person.name)
        contact_num = request.data.get('contact_num', None)
        serializer = self.serializer_class(profile, data=request.data)

        if serializer.is_valid():
            if contact_num is not None:
                if str(contact_num) not in str(profile.contact_num):
                    if Profile.objects.filter(contact_num=contact_num).count():
                        return Response({ "contact_num": ["User with this Phone Number already exists."]},
                                        status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            person.name = name
            person.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileImageView(generics.RetrieveUpdateAPIView):
    """
        Profile Image View
        owner_id -- Owner ID for Pofile Image
    """

    model = ProfileImage
    serializer_class = ProfileImageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        
        if request.GET.get("owner_id",None):
            profile_image = self.model.objects.get(owner_id=request.GET['owner_id'])
        else:
            profile_image = get_object_or_404(self.model,owner=request.owner)    
        serializer = self.serializer_class(profile_image)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        profile_image = self.model.objects.get(owner=request.user)
        serializer = self.serializer_class(profile_image, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
