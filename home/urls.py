from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("projects", views.projects, name='projects'),
    
    path("register", views.register, name='register'),
    path("login", views.login, name='login'),  
    path('signup', views.handleSignUp, name="handleSignUp"),  

]