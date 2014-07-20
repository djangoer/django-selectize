from django.shortcuts import render
from django.views.generic.edit import CreateView
#from django.core.urlresolvers import reverse
from app1.models import ArticleForm,Article
# Create your views here.
class ArticleView(CreateView):
    form_class = ArticleForm
    success_url = '/tests/articles/'
    template_name = 'articles.html'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Article.objects.order_by('id')
        return super(ArticleView, self).get_context_data(**kwargs)