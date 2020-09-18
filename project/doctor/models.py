from django.db import models

# Create your models here.
class Contact(models.Model):
	sno=models.AutoField(primary_key=True)
	name=models.CharField(max_length=250)
	email=models.CharField(max_length=250)
	content=models.CharField(max_length=300)
	
	
	def __str__(self):
		return "message from "+self.name
