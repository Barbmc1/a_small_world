"""Defines the URL patterns for users."""

from django.urls import path
from django.contrib.auth.views import auth_login 

from . import views

app_name = 'users'
urlpatterns = [
    #Login page
    path('login/', auth_login, {'template_name:' 'users/login.html'}, name='login'),
    #Logout page
    path('logout/',  views.logout_view, name='logout'),
    #Registration Page
    path('register/', views.register, name='register'),
]

