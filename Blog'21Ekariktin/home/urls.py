from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home, name = 'home'),
    path('Contact',views.Contact, name = 'Contact'),
    path('about',views.about, name = 'about'),
    path('search',views.search, name = 'search'),
    path('signup',views.handlesignup, name = 'handlesignup'),
    path('login',views.handlelogin, name = 'handlelogin'),
    path('logout',views.handlelogout, name = 'handlelogout'),
    
 
]