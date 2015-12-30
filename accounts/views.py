from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, logout, authenticate
from rest_framework import generics, permissions, status
from django.contrib.sites.models import get_current_site
from person.models import Profile,ProfileImage,Fblogin,Googlelogin
from django.conf import settings
from accounts.serializers import RegisterSerializer, LoginSerializer, PassChangeSerializer,FacebookSerializer,GoogleSerializer
from django.utils import timezone

User = get_user_model()


class Login(generics.GenericAPIView):
    """
        Login a existing user to system
    """
    serializer_class = LoginSerializer
    token_model = Token
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = authenticate(email=serializer.data['email'],
                                password=serializer.data['password'])
            if user and user.is_authenticated():
                if user.is_active:
                    #login(request, user)
                    
                    token = self.token_model.objects.get_or_create(user=user)[0].key
                    
                    # Update last login time
                    user.last_login = timezone.now()
                    user.save(update_fields=['last_login'])
                    return Response({'token': token,
                                     'name': user.name,
                                     #'contact_num': user.contact_num,
                                     'email': user.email,
                                     },
                                    status = status.HTTP_200_OK)
                else:
                    return Response({'error': ['This account is disabled.']},
                                    status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error': ['Invalid Username/Password.']},
                                status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class Register(APIView):
    """
        Register a new user to system
    """
    
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)
    model = User

    def get_serializer_class(self):
        return self.serializer_class

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            try:
                user = authenticate(email=user.email,
                                    password=request.data['password'])
            except User.MultipleObjectsReturned:
                users = User.objects.filter(email=user.email)
                for u in users[1:]:
                    u.is_active = False
                    u.save()
                user = users[0]

            token, created = Token.objects.get_or_create(user=user)
            
            Profile(owner=user).save()
            ProfileImage(owner=user).save()
            current_site = get_current_site(request)
            domain = current_site.domain
                
            ''''q = UserRegistered()
            q.delay(ctx={'user_id':user.id,
                         'first_name': user.first_name,
                         'domain': domain,
                         'protocol': settings.PROTOCOL})
'''
            return Response({'token': token.key, 
                             'name': user.name},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
            
class Logout(APIView):
    """
        Logout a logged in user to system
    """    

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        
        try:
            logout(request)
            return Response({'success': 'Successfully logged out.'},
                            status=status.HTTP_200_OK)
        except Exception, e:
            print e
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)            

class ChangePassword(APIView):
    """
        Change User password to new one
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PassChangeSerializer
    model = User

    def get_serializer_class(self):
        return self.serializer_class

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if request.user.check_password(serializer.data['old_password']):
                request.user.set_password(serializer.data['new_password'])
                request.user.save()
                
                return Response({'success': 'Password successfully changed'},
                                status=status.HTTP_200_OK)
            else:
                return Response({'error': ['Old password does not match']},
                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthLogin(APIView):
    
    #serializer_class = FacebookSerializer
    permission_classes = (permissions.AllowAny,)
    #model = Fblogin
    user_model = User
    token_model = Token
    
    def get_serializer_class(self):
        return self.serializer_class
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                un_id = self.model.objects.get(un_id=serializer.data['un_id'])
                if un_id.owner.is_active:
                    token = self.token_model.objects.get_or_create(user=un_id.owner)[0].key
                    un_id.owner.last_login = timezone.now()
                    un_id.owner.save(update_fields=['last_login'])
                    return Response({'token': token,
                                     'name': un_id.owner.name,
                                     'email': un_id.owner.email,
                                     },
                                    status = status.HTTP_200_OK)
                else:
                    return Response({'error': ['This account is disabled.']},
                                    status=status.HTTP_401_UNAUTHORIZED)
            except self.model.DoesNotExist:
                user,created = self.user_model.objects.get_or_create(email=serializer.data['email'])
                if created:
                    user.name = serializer.data['name']
                    user.is_active=True
                    user.save()    
                    Profile(owner=user).save()
                    ProfileImage(owner=user).save()
                try:    
                    obj,creat=self.model.objects.get_or_create(un_id=serializer.data['un_id'],owner=user)
                    if not creat:
                        return Response({'error':'This token or email ID is already associated with other email ID or token resp.'},\
                                    status=status.HTTP_400_BAD_REQUEST)
                except:
                    return Response({'error':'This token or email ID is already associated with other email ID or token resp.'},\
                                    status=status.HTTP_400_BAD_REQUEST)    
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 
                                 'name': user.name,
                                 'email':user.email},
                                 status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)    

class Fblogin(AuthLogin):
    serializer_class = FacebookSerializer
    model = Fblogin            


class GoogleLogin(AuthLogin):
    serializer_class = GoogleSerializer
    model = Googlelogin
