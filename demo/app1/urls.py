from django.conf.urls import url
from django.views.generic import TemplateView

from app1.views import ArticleView
urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="home.html"),name='home'),
	url(r'^articles/$', ArticleView.as_view(),name='articles'),
]