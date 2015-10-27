from django.conf.urls import patterns, url
from local import views

urlpatterns = patterns('',
                       
                       url(r'^tag-friend/$', views.TagFriendView.as_view(), name='TagFriend'),
                       url(r'^feedback-stats/$',views.FeedbackCount.as_view(),name='Feedback-Statistics'),

                       #url(r'^images/$', views.UploadImageShow.as_view(), name='UploadImagesShow'),    
                       url(r'^local-feed-reviews/$', views.LocalFeedReview.as_view(), name='LocalFeedReview'),
                       url(r'^local-feed-images/$', views.LocalFeedImages.as_view(), name='LocalFeedReview'),
                       )