from django.shortcuts import render
from . import forms
from app1.models import User
from app1.forms import SignupForm
from django.contrib.auth.hashers import make_password

# Create your views here.
def home(request):
    return render(request,'app1/home.html')

def login(request):
    return render(request,'app1/login.html')

def about(request):
    return render(request,'app1/about.html')

def signup(request):

    user_form = SignupForm

    registered = False

    if request.method == 'POST':
        user_form = SignupForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.password = make_password(user.password)
            user.save()

            registered = True

        else:
            print('user_form.errors')

    return render(request, 'app1/signup.html', {'form':user_form, 'registered':registered})