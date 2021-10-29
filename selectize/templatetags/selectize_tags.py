from django import template
# from django.templatetags.static import static
# see stackoverflow :http://stackoverflow.com/questions/11721818
from django.templatetags.static import static 
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def selectize_tags_media(media_type='css',name=''):
	"""
	Usage:
	------
	To include css media:
	selectize_tags_media 'css' <theme>

	To include Selectize Scripts:
	selectize_tags_media 'js'

	To include Selectize Scripts and Jquery:
	selectize_tags_media 'js' 'jquery'
	"""
	if media_type=='js':
		str_script='<script src="{url}"></script>\n'
		html=str_script.format(url=static('selectize/selectize.min.js'))
		if name=='jquery':
			html=str_script.format(url=static('selectize/jquery.min.js'))+html
		return mark_safe(html)

	if name:name+='.'
	fpath='selectize/css/selectize.{name}css'.format(name=name)
	return mark_safe('<link rel="stylesheet" href="{url}">'.format(url=static(fpath)))