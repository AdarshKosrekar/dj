#from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Employee(models.Model):
	eid=models.CharField(max_length=20)
	ename=models.CharField(max_length=100)
	econtact=models.CharField(max_length=15)
	'''contact=models.IntegerField()
	email=models.EmailField(max_length=50)
	age=models.IntegerField()'''
	class Meta:
		db_table="employee"
