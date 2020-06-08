from django.shortcuts import render
from . import forms
from accounts.models import User
from accounts.forms import SignupForm
from django.contrib.auth.hashers import make_password

# Create your views here.
def home(request):
    return render(request,'accounts/home.html')

def login(request):
    return render(request,'accounts/login.html')

def about(request):
    return render(request,'accounts/about.html')

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

    return render(request, 'accounts/signup.html', {'form':user_form, 'registered':registered})
