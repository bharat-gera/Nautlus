from django.conf.urls import patterns,url
from places import views

urlpatterns = patterns('',
                       
                       url('^bookmarked/$',views.BookmarkedView.as_view(),name='Bookmarked'),
                       url('^bookmarked/edit/(?P<pk>[0-9]+)/$',views.BookmarkedEditView.as_view(),name='BookmarkedEdit'),
                       
                       url('^beenhere/$',views.BeenhereView.as_view(),name='Beenhere'),
                       url('^beenhere/edit/(?P<pk>[0-9]+)/$',views.BeenhereEditView.as_view(),name='BeenhereEdit'),
                       
                       url('^favourite/$',views.FavouritesView.as_view(),name='Favourite'),
                       url('^favourite/edit/(?P<pk>[0-9]+)/$',views.FavouritesEditView.as_view(),name='FavouriteEdit'),
                       
                       )

