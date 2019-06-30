from django.db import models

# Create your models here.


class URLMap(models.Model):

	url   		= models.CharField(max_length=512)
	identifier 	= models.PositiveIntegerField()
	created_on 	= models.DateTimeField(auto_now=True)
