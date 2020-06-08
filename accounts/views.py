from django.shortcuts import render
from . import forms
from accounts.models import User
from accounts.forms import SignupForm
from django.contrib.auth.hashers import make_password

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'accounts/home.html')

# def login(request):
#     return render(request,'accounts/login.html')

def about(request):
    return render(request,'accounts/about.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:home'))

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

def user_login(request):

    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('accounts:home'))

            else: 
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request, 'accounts/login.html', {})