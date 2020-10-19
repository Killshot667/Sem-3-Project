from django.urls import path
from . import views
urlpatterns = [
	path('', views.home,name = 'doctorHome'),
	path('contact/', views.contact,name = 'contact'),
	path('about/', views.about,name = 'about'),
	path('signup/', views.handleSignup,name = 'signup'),
	path('dashboard/<str:pk>',views.dashboard,name = 'dashboard'),

	path('login', views.handeLogin, name = "handleLogin"),
	path('logout', views.handelLogout, name = "handleLogout"),
]