from django.conf.urls import patterns, url
from feedback import views

urlpatterns = patterns('',
                       
                       url(r'^$', views.ReviewShowDetail.as_view(), name='ReviewShow'),
                       url(r'^(?P<place_id>[-\w]+)/$', views.ReviewDetailView.as_view(), name='ReviewDetail'),
                       url(r'^edit/(?P<pk>[0-9]+)/$', views.ReviewEditView.as_view(), name='ReviewEdit'),
                       
                       url(r'^comment/(?P<pk>[0-9]+)/$', views.ReviewCommentView.as_view(), name='ReviewComment'),
                       url(r'^comment/edit/(?P<id>[0-9]+)/$', views.ReviewCommentEdit.as_view(), name='ReviewCommentEdit'),
                       
                       url(r'^review-like/(?P<pk>[0-9]+)/$', views.ReviewLikeView.as_view(), name='ReviewLike'),
                       url(r'^review-unlike/edit/(?P<pk>[0-9]+)/$', views.ReviewLikeEditView.as_view(), name='ReviewEdit'),
                       
                       url(r'^comment-like/(?P<id>[0-9]+)/$', views.CommentLikeView.as_view(), name='CommentLike'),
                       url(r'^comment-unlike/edit/(?P<id>[0-9]+)/$', views.CommentLikeEditView.as_view(), name='CommentLikeEdit'),
                       
                       
                       )