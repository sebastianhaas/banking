from django.conf.urls import patterns, include, url
from django.contrib import admin
from webservice import views

urlpatterns = patterns('',
                       url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
                       url(r'^account/$', views.AccountList.as_view()),
                       url(r'^admin/', include(admin.site.urls)),
                       )
