from django.conf.urls import url
from app1.views import ArticleAdd,ArticleUpdate

urlpatterns = [
	url(r'^articles/add/$', ArticleAdd.as_view(),name='articles'),
	url(r'^articles/(?P<pk>[0-9]+)/$', ArticleUpdate.as_view(), name='article_update'),
]