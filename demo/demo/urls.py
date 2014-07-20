from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^tests/', include('app1.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
