from django import views
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("" ,  index  , name="index"),
    path("login", login , name="login"),
    path("register", register , name="register"),
    path("loggedin", loggedin , name="loggedin"),
    path("farmerslogin", farmerslogin , name="farmerslogin")
]
