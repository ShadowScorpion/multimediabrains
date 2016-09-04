from django.db import models

class Users(models.Model):
	username = models.CharField(max_length=30)
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	email_address = models.CharField(max_length=30)
	id_pk = models.IntegerField(default=0)
	scores = models.IntegerField(default=0)
	photo = models.CharField(max_length=50)
	create_date = models.DateTimeField('date')
