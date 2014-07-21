[django-selectize](http://selectize-djangoer.rhcloud.com/)
=================

Note: This is only in Developing stage Now.

django-selectize  is a Django app based on Selectize.js that help you to create Select and Multiselect widgets in Django forms.


Requirements
------------

* Django


Installing django-selectize
---------------------------

There are several ways to install django-selectize:

* Automatically, via a package manager: `pip install django-selectize`
* Download a release package then unzip and run `python setup.py install` to install it into your python directory.
* If you don't like to install then download a release package, unzip and copy the folder `selectize` to your Django-project directory.


Required settings
-----------------

Begin by adding `selectize` to the `INSTALLED_APPS` setting of your project. For example, you might have something like the following in your Django settings file:

	INSTALLED_APPS = (
	    'django.contrib...',
	    'django.contrib....',
	    'selectize',
	    # ...other installed applications...
	)

**Note:** you must place `selectize` above other installed applications.

Usage
-----

In templates, load the `selectize_tags`::

	{% load selectize_tags %}

To include selectize.default.css:

	{% selectize_tags_media 'css' 'default' %}

which will return:

    <link rel="stylesheet" href="{% static "selectize/css/selectize.default.css" %}">

Like wise you can include selectice.js by:
	
	{% selectize_tags_media 'js' 'selectize' %}

Also if you want to include the jquery file packed with django-selectize,:

    {% selectize_tags_media 'js' 'jquery' %}


Now Intiate a selectize box from a normal selectbox by calling:

	<script>$('#id_publications').selectize();</script>


Full Example
------------

For testing
-----------
You need to install Selenium:

    pip install selenium

Run the tests:

    ./manage.py test
