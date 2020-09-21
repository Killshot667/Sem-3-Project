from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='doctorHome'), 	
    path('contact/', views.contact,name='contact'), 	
    path('about/', views.about,name='about'), 	
]
