from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
	sno=models.AutoField(primary_key=True)
	name=models.CharField(max_length=250)
	email=models.CharField(max_length=250)
	content=models.CharField(max_length=300)
	
	
	def __str__(self):
		return "message from "+self.name
class Doctor(models.Model):
	user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
	profile_pic=models.ImageField(upload_to='images/profile', default="")
	
	
	def __str__(self):
		return self.user.first_name + self.user.last_name