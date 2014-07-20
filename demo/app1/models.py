from django.db import models

# Create your models here.
# This sample is taken from 
# https://docs.djangoproject.com/en/dev/topics/db/examples/many_to_many/
class Publication(models.Model):
	title = models.CharField(max_length=30)
	def __str__(self):              # __unicode__ on Python 2
		return self.title
	class Meta:
		ordering = ('title',)

class Article(models.Model):
	headline = models.CharField(max_length=100)
	publications = models.ManyToManyField(Publication)
	ratings= models.IntegerField(max_length=1,choices=((0, 'Bad'),(1, 'Average'),
		(2, 'Good'),(3, 'Outstanding')),default=1)	