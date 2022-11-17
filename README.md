## Django Selectize

django-selectize  is a Django app based on Selectize.js that help you to create Select and Multiselect widgets in Django forms.

## Installation

Install `django-selectize`:

    pip install django-selectize



Add `django-selectize` to your `INSTALLED_APPS` in your project settings.

    INSTALLED_APPS = [
        # other django apps...
        'django_selectize',
    ]

## Quick Start

Here is a quick example to get you started:

We have the following model:

    # models.py
    from django.conf import settings
    from django.db import models

    class Book(models.Model):
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        co_authors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='co_authored_by')


Next, we create a model form with custom Selectize widgets.

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


A simple class based view will do, to render your form:

    # views.py
    from django.views import generic

    from . import forms, models

    class BookCreateView(generic.CreateView):
        model = models.Book
        form_class = forms.BookForm
        success_url = "/"

Make sure to add the view to your `urls.py`:

    # urls.py
    from django.urls import include, path
    from . import views

    urlpatterns = [
        # ... other patterns
        path("", views.BookCreateView.as_view(), name="book-create"),
    ]


Finally, we need a little template, `myapp/templates/myapp/book_form.html`

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Create Book</title>
        {{ form.media.css }}
        <style>
            input, select {width: 100%}
        </style>
    </head>
    <body>
        <h1>Create a new Book</h1>
        <form method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit">
        </form>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        {{ form.media.js }}
    </body>
    </html>

