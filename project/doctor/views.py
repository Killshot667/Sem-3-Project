from django.shortcuts import render,redirect
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



def handleSignup(request):
	if(request.method=='POST'):

		username=request.POST['name']
		email=request.POST['email']
		pass1=request.POST['pass1']
		pass2=request.POST['pass2']
		if pass1!=pass2:
			# TODO: write code...
			
			messages.error(request,"please fill form correctly")
			return redirect('doctorHome')
	
	
			
		
		myuser=User.objects.create_user(username,email,pass1)
		myuser.save()
		messages.success(request,"Your Account is successfully created!!!")
		return redirect('doctorHome')
	
	