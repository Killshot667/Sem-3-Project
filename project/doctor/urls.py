from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='doctorHome'), 	
    path('contact/', views.contact,name='contact'), 	
    path('about/', views.about,name='about'), 	
    path('signup/', views.handleSignup,name='signup'), 	
    path('doctors_list/',views.DoctorListView.as_view(),name='doctors_list')
]
