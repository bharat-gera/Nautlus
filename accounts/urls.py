from accounts import views
from django.conf.urls import patterns, url
from person.views import ProfileView,ProfileImageView
urlpatterns = patterns('',

    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^fb-login/$', views.Fblogin.as_view(), name='fb-login'),
    url(r'^google-login/$', views.GoogleLogin.as_view(), name='google-login'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^profile-image/$', ProfileImageView.as_view(), name='profile_image'),
    
    url(r'^change-password/$', views.ChangePassword.as_view(), name='logout'),
    
    )