from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    url(r'^tests/', include('app1.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
