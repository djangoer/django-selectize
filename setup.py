try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(name='django-selectize',
	version='1.0',
	description='django-selectize is a Django app based on Selectize.js that help you to create Select and Multiselect widgets in Django forms.',
    author='Djangoer',
    author_email='djangoer0@gmail.com',
    url='https://github.com/djangoer/django-selectize',
	packages=['selectize'],#py_modules=['modoscript'],
	install_requires=[
		"Django",	
	],
)