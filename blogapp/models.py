from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class reservations(models.Model):
	date_from = models.DateField()
	date_to = models.DateField()
	room_type = models.CharField(max_length = 50)
	adults = models.CharField(max_length = 20)
	children = models.CharField(max_length = 20)
	name = models.CharField(max_length = 300)
	gender = models.CharField(max_length = 20)
	email = models.CharField(max_length = 300)
	phone = models.CharField(max_length = 20)
	age = models.CharField(max_length = 20)
	cnic = models.CharField(max_length = 50)
	method = models.CharField(max_length = 50)


class foodorders(models.Model):
	name = models.CharField(max_length = 50)
	room = models.CharField(max_length = 5)
	items = models.CharField(max_length = 50)
	cnic = models.CharField(max_length = 50)

class feedbacks(models.Model):

	cnic = models.CharField(max_length = 50)

	feed = models.TextField(max_length = 500)





