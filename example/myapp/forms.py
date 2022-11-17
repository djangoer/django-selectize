# forms.py
from django import forms
from django_selectize import forms as s2forms

from . import models


class AuthorWidget(s2forms.SelectizeWidget):
    search_fields = [
        "username__icontains",
        "email__icontains",
    ]


class CoAuthorsWidget(s2forms.SelectizeMultipleWidget):
    search_fields = [
        "username__icontains",
        "email__icontains",
    ]


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"
        widgets = {
            "author": AuthorWidget,
            "co_authors": CoAuthorsWidget,
        }
