from django import forms
from django.utils.safestring import mark_safe

def render_js_script(inner_code):
    return u"""
    <script type="text/javascript">
        jQuery(function ($) {
            %s
        });
    </script>""" % inner_code

class SelectizeWidget(forms.Select):
    """    
    Example::
    
    from selectize.widgets import SelectizeWidget
    from django.forms import ModelForm

    class MyForm(ModelForm):
        class Meta:
            model = MyModel
            widgets = {
                'name': SelectizeWidget()
            }
    """

    def render(self, name, value, attrs=None):
        s = unicode(super(SelectizeWidget, self).render(name, value,attrs))
        #attrs = self.build_attrs(attrs, multiple='multiple')
        #s = unicode(super(MultipleSelect2HiddenInput, self).render(name, u"", attrs))
        id_ = attrs.get('id', None)

        if id_:
            jscode = u"$('#%s').selectize();" % id_            
            s += render_js_script(jscode)
        else:s+='<!--noid-->'
        return mark_safe(s)
    def value_from_datadict(self, data, files, name):
        #if isinstance(data, (MultiValueDict, MergeDict)):return data.getlist(name)
        value = data.get(name, None)
        if value:return value.split(',')
        return value