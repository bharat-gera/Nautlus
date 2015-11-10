from django.conf.urls import patterns,url
from places import views

urlpatterns = patterns('',
                       
                       url('^bookmarked/$',views.BookmarkedListView.as_view(),name='BookmarkedList'),
                       url('^(?P<place_id>[-\w]+)/bookmarked/$',views.BookmarkedView.as_view(),name='Bookmarked'),
                       url('^bookmarked/edit/(?P<pk>[0-9]+)/$',views.BookmarkedEditView.as_view(),name='BookmarkedEdit'),
                       
                       url('^beenhere/$',views.BeenHereListView.as_view(),name='BeenhereList'),
                       url('^(?P<place_id>[-\w]+)/beenhere/$',views.BeenHereView.as_view(),name='Bookmarked'),
                       url('^beenhere/edit/(?P<pk>[0-9]+)/$',views.BeenhereEditView.as_view(),name='BeenhereEdit'),
        
                       url('^favourite/$',views.FavouriteListView.as_view(),name='favouriteList'),
                       url('^(?P<place_id>[-\w]+)/favourite/$',views.FavouriteView.as_view(),name='favourite'),
                       url('^favourite/edit/(?P<pk>[0-9]+)/$',views.FavouriteEditView.as_view(),name='favouriteEdit'),
                       
                       url('^follow/$',views.FollowFriendsView.as_view(),name='followList'),
                       url('^unfollow/(?P<following_id>[0-9]+)/$',views.FollowFriendsEdit.as_view(),name='followListEdit'),
                       )

