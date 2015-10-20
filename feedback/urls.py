from django.conf.urls import patterns, url
from feedback import views

urlpatterns = patterns('',
                       
                       url(r'^$', views.ReviewDetailView.as_view(), name='ReviewDetail'),
                       url(r'^(?P<pk>[0-9]+)/$', views.ReviewEditView.as_view(), name='ReviewEdit'),
                       
                       url(r'^comment/(?P<pk>[0-9]+)/$', views.ReviewCommentView.as_view(), name='ReviewComment'),
                       url(r'^comment/edit/(?P<id>[0-9]+)/$', views.ReviewCommentEdit.as_view(), name='ReviewCommentEdit'),
                       
                       url(r'^review-like/(?P<pk>[0-9]+)/$', views.ReviewLikeView.as_view(), name='ReviewLike'),
                       url(r'^review-unlike/edit/(?P<pk>[0-9]+)/$', views.ReviewLikeEditView.as_view(), name='ReviewEdit'),
                       
                       url(r'^comment-like/(?P<id>[0-9]+)/$', views.CommentLikeView.as_view(), name='CommentLike'),
                       url(r'^comment-unlike/edit/(?P<id>[0-9]+)/$', views.CommentLikeEditView.as_view(), name='CommentLikeEdit'),
                       
                       url(r'^upload-image/$', views.UploadImageView.as_view(), name='UploadImage'),
                       url(r'^upload-image/(?P<pk>[0-9]+)/$', views.UploadImageEdit.as_view(), name='UploadImageEdit'),
                       
                       url(r'^upload-image-like/(?P<pk>[0-9]+)/$', views.UploadImageLikeView.as_view(), name='UploadImageLike'),
                       url(r'^upload-image-unlike/edit/(?P<pk>[0-9]+)/$', views.UploadImageLikeEdit.as_view(), name='UploadImageLikeEdit'),
                       
                       url(r'^image-comment/(?P<pk>[0-9]+)/$', views.UploadImageComment.as_view(), name='ImageComment'),
                       url(r'^image-comment/edit/(?P<pk>[0-9]+)/$', views.UploadImageCommentEdit.as_view(), name='ImageCommentEdit'),
                       
                       url(r'^image-comment-like/(?P<pk>[0-9]+)/$', views.UploadImageCommentLike.as_view(), name='ImageCommentLike'),
                       url(r'^image-comment-like/edit/(?P<pk>[0-9]+)/$', views.UploadImageCommentLikeEdit.as_view(), name='ImageCommentLikeEdit'),
                       
                       url(r'^tag-friend/$', views.TagFriendView.as_view(), name='TagFriend'),
                       url(r'^feedback-stats/$',views.FeedbackCount.as_view(),name='Feedback-Statistics'),

                       url(r'^read-only/$', views.ReviewShowDetail.as_view(), name='ReviewShow'),
                       url(r'^images/$', views.UploadImageShow.as_view(), name='UploadImagesShow'),                       
                       )