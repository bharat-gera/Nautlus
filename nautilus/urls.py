from django.conf.urls import patterns, include, url
from django.contrib import admin
from apiset import ApiSet
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

apiv1 = ApiSet(
               urls=[
                     url(r'^accounts/', include('accounts.urls')),
                     url(r'^search/', include('search.urls')),
                     url(r'^feedback/', include('feedback.urls')),  
                     url(r'^places/',include('places.urls')),
                     url(r'^local/',include('local.urls')),
                     url(r'^wallet/',include('wallet.urls')),
                     url(r'^uploadimages/',include('uploadimages.urls')),
                     url(r'^order/',include('order.urls')),                   
                     url(r'^docs/', include('rest_framework_swagger.urls'))
                     ]
               )



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tagfe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^api/v1/', include(apiv1)),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
