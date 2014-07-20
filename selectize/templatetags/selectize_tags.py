from django import template
# from django.templatetags.static import static
# see stackoverflow :http://stackoverflow.com/questions/11721818
from django.contrib.staticfiles.templatetags.staticfiles import static 

register = template.Library()

@register.simple_tag
def selectize_tags_media(media_type='css',name=''):
	if media_type=='js':
		html='<script src="{url}"></script>'		
		fpath='selectize/{name}.min.js'.format(name=name)
	else:
		html='<link rel="stylesheet" href="{url}">'
		fpath='selectize/css/selectize.{name}.css'.format(name=name)
	return html.format(url=static(fpath))