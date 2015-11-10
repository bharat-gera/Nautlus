from django.conf.urls import patterns, url
from wallet import views

urlpatterns = patterns('',
                       
                       url(r'^$', views.WalletDetail.as_view(), name='WalletDetail'),
                       url(r'^recharge/$', views.RechargeRequest.as_view(), name='RechargeDetail'),
                       
                       )
