from django.db import models

# Create your models here.
class Login(models.Model):
	username=models.CharField(max_length=20)
	password=models.CharField(max_length=20)

	class Meta:
		db_table='Login'
class Register(models.Model):
	username=models.CharField(max_length=20)
	address=models.CharField(max_length=80)
	pin=models.CharField(max_length=10)
	firstname=models.CharField(max_length=20)
	lastname=models.CharField(max_length=20)

	class Meta:
		db_table='Register'