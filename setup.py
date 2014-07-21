try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(name='django-selectize',
	version='1.2',
	description='django-selectize is a Django app based on Selectize.js that help you to create Select and Multiselect widgets in Django forms.',
    author='Djangoer',
    author_email='djangoer0@gmail.com',
    url='https://github.com/djangoer/django-selectize',
	packages=['selectize','selectize.templatetags'],#py_modules=['modoscript'],
	include_package_data=True,#package_data = {'package' : ["selectize/static/*"] },
	install_requires=[
		"Django",	
	],
	zip_safe=False,
)
