from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Contact
# Create your views here.
def home(request):
	return render(request,'doctor/home.html')
	
def about(request):
	# return HttpResponse('hr')
	return render(request,'doctor/about.html')
	
def contact(request):
	# name=request.post['name']
	if(request.method=='POST'):
		name=request.POST['name']
		email=request.POST['email']
		content=request.POST['content']
		contact=Contact(name=name,email=email,content=content)
		contact.save()
		messages.success(request,"Your query is sent successfully !!!")
		
	return render (request,"doctor/contact.html")
