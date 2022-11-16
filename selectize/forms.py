from django import forms
from itertools import chain



class SelectizeMixin:
    """
    The base mixin of all Selectize widgets.

    This mixin is responsible for rendering the necessary
    data attributes for selectize as well as adding the static
    form media.
    """

    css_class_name = "django-selectize"
    theme = None

    empty_label = ""

    

    def build_attrs(self, base_attrs, extra_attrs=None):
        """Add selectize data attributes."""
        default_attrs = {
            "data-minimum-input-length": 0,
        }
        if self.is_required:
            default_attrs["data-allow-clear"] = "false"
        else:
            default_attrs["data-allow-clear"] = "true"
            default_attrs["data-placeholder"] = self.empty_label or ""

        default_attrs.update(base_attrs)
        attrs = super().build_attrs(default_attrs, extra_attrs=extra_attrs)

        if "class" in attrs:
            attrs["class"] += " " + self.css_class_name
        else:
            attrs["class"] = self.css_class_name
        return attrs

    def optgroups(self, name, value, attrs=None):
        """Add empty option for clearable selects."""
        if not self.is_required and not self.allow_multiple_selected:
            self.choices = list(chain([("", "")], self.choices))
        return super().optgroups(name, value, attrs=attrs)

    @property
    def media(self):
        """
        Construct Media as a dynamic property.

        .. Note:: For more information visit
            https://docs.djangoproject.com/en/stable/topics/forms/media/#media-as-a-dynamic-property
        """
        
        return forms.Media(
            js=["django_selectize/selectize.min.js","django_selectize/django_selectize.js"],
            css={"screen": ["django_selectize/selectize.css"]},
        )

class SelectizeWidget(SelectizeMixin, forms.Select):
    """
    Selectize drop in widget.

    Example usage::

        class MyModelForm(forms.ModelForm):
            class Meta:
                model = MyModel
                fields = ('my_field', )
                widgets = {
                    'my_field': SelectizeWidget
                }

    or::

        class MyForm(forms.Form):
            my_choice = forms.ChoiceField(widget=SelectizeWidget)

    """