from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from django.core.urlresolvers import reverse_lazy
#from django.core.urlresolvers import reverse
from app1.models import Article
# Create your views here.

class ArticleView(object):
    model = Article#form_class = ArticleForm
    success_url = reverse_lazy('articles')
    template_name = 'articles.html'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Article.objects.order_by('id')
        return super(ArticleView, self).get_context_data(**kwargs)

class ArticleAdd(ArticleView,CreateView):
	pass

class ArticleUpdate(ArticleView,UpdateView):
	pass