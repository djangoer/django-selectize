
from app1.views import ArticleAdd,ArticleUpdate
from django.urls import path
urlpatterns = [
	path('articles/add/', ArticleAdd.as_view(),name='articles'),
	path('articles/<int:pk>/', ArticleUpdate.as_view(), name='article_update'),
]