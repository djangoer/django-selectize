from django.shortcuts import render

# Create your views here.
# views.py
from django.views import generic

from . import forms, models


class BookCreateView(generic.CreateView):
    model = models.Book
    form_class = forms.BookForm
    success_url = "/"
