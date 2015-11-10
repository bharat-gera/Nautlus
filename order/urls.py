from django.conf.urls import patterns, include, url
from order import views

urlpatterns = patterns('',
                       url(r'^$', views.OrderDetail.as_view(), name='OrderDetail'),
                       
                       )