from django.conf.urls import patterns, include, url
from django.contrib import admin
from webservice import views

urlpatterns = patterns('',
                       url(r'^balance_sheet_account/$', views.BalanceSheetAccountList.as_view()),
                       url(r'^admin/', include(admin.site.urls)),
                       )
