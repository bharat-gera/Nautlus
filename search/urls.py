from django.conf.urls import patterns, include, url
from search import views

urlpatterns = patterns('',
                       
    url (r'^$',views.SimpleSearch.as_view()), 
    url (r'^detail/$',views.DetailSearchView.as_view()),
    url (r'^auto/$',views.AutoCompleteSearchView.as_view()),
    #url (r'^images/$',views.GoogleImagesView.as_view()),
    url (r'^category/$',views.ServiceCategoryView.as_view())
    
    )