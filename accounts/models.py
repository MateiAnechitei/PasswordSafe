from django.db import models

# Create your models here.
class Account(models.Model):
	owner_id = models.IntegerField(blank = True, null = True)
	site = models.CharField(max_length = 255, blank = True, null =True)
	username = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)



