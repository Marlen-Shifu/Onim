from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('filter/category=<str:category>', views.index),

	path('new_offer', views.add_offer_form),
	path('add_offer', views.add_offer),

	path('register', views.Register_User_form),
	path('register_user', views.Register_User),

	path('login', views.Login_User_form),
	path('login_user', views.Login_User),

	path('profile', views.view_profile),
]