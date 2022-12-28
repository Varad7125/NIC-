from accounts.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User , auth
from .models import *
from django.conf import settings
import psycopg2

conn = psycopg2.connect(
   database="user_management", user='postgres', password='varad', host='127.0.0.1', port= '5432'
)
cur = conn.cursor()


def index(request):
    return render(request , 'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
    else:
        return render(request, 'login.html')


def loggedin(request):
    return render(request, 'loggedin.html')

def farmerslogin(request):
    return render(request, 'farmers.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save();
        print('user created')
        return render(request , 'login.html')

    else:
        return render(request , 'register.html') 
    