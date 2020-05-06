from django.db import models


# Create your models here.
class Employee(models.Model):
	fullname = models.CharField(max_length=100)
	emp_id = models.IntegerField()
	mobile = models.CharField(max_length=15)
