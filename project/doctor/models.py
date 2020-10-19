from django.db import models
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
	sno=models.AutoField(primary_key=True)
	name=models.CharField(max_length=250)
	email=models.CharField(max_length=250)
	content=models.CharField(max_length=300)
	
	
	def __str__(self):
		return "message from "+self.name
class Speciality(models.Model):
	spec=models.CharField(max_length=100,help_text='Enter speciality')
	class Meta:
		verbose_name='Speciality'
	def __str__(self):
		return self.spec
	
class Doctor(models.Model):
	sno=models.AutoField
	name=models.CharField(max_length=100,help_text='enter name')
	speciality=models.ManyToManyField(Speciality,help_text='chose your specialities') 
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('doctor-detail',args=[str(self.ind)])
