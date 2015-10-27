from django.conf.urls import patterns, url
from uploadimages import views

urlpatterns = patterns('',
                       
                       url(r'^upload-image/$', views.UploadImageShow.as_view(), name='UploadImageShow'),
                       url(r'^upload-image/(?P<place_id>[-\w]+)/$', views.UploadImageView.as_view(), name='UploadImage'),
                       url(r'^upload-image/edit/(?P<pk>[0-9]+)/$', views.UploadImageEdit.as_view(), name='UploadImageEdit'),
                       
                        url(r'^upload-image-like/(?P<pk>[0-9]+)/$', views.UploadImageLikeView.as_view(), name='UploadImageLike'),
                       url(r'^upload-image-unlike/edit/(?P<pk>[0-9]+)/$', views.UploadImageLikeEdit.as_view(), name='UploadImageLikeEdit'),
                       
                       url(r'^image-comment/(?P<pk>[0-9]+)/$', views.UploadImageComment.as_view(), name='ImageComment'),
                       url(r'^image-comment/edit/(?P<pk>[0-9]+)/$', views.UploadImageCommentEdit.as_view(), name='ImageCommentEdit'),
                       
                       url(r'^image-comment-like/(?P<pk>[0-9]+)/$', views.UploadImageCommentLike.as_view(), name='ImageCommentLike'),
                       url(r'^image-comment-like/edit/(?P<pk>[0-9]+)/$', views.UploadImageCommentLikeEdit.as_view(), name='ImageCommentLikeEdit'),
                       
                       
                       
                       )
                       