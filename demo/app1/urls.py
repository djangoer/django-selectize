
from app1.views import ArticleAdd,ArticleUpdate
from django.urls import path
urlpatterns = [
	path('articles/add/', ArticleAdd.as_view(),name='articles'),
	path('articles/(?P<pk>[0-9]+)/', ArticleUpdate.as_view(), name='article_update'),
]