from django.shortcuts import render
from . import forms
from accounts.models import User
from accounts.forms import SignupForm
from django.contrib.auth.hashers import make_password

#
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

login_flag = False

# Create your views here.
def home(request):
    return render(request,'accounts/home.html', {'login_flag':login_flag})

# def login(request):
#     return render(request,'accounts/login.html')

def about(request):
    return render(request,'accounts/about.html', {'login_flag':login_flag})

# @login_required
def user_logout(request):
    # logout(request)
    global login_flag
    login_flag = False
    return HttpResponseRedirect(reverse('accounts:home'))

def signup(request):

    global login_flag

    user_form = SignupForm

    registered = False

    if request.method == 'POST':
        user_form = SignupForm(data=request.POST)

        if user_form.is_valid():
            user_form.save()
            # user.password = make_password(user.password)
            # user.save()

            registered = True
            login_flag = True

        else:
            print('user_form.errors')

    return render(request, 'accounts/signup.html', {'form':user_form, 'registered':registered})

def user_login(request):

    global login_flag

    if request.method == 'POST': 
        usrname = request.POST.get('username')
        passwrd = request.POST.get('password')

        print(User.objects.filter(username=usrname).exists())
        if User.objects.filter(username=usrname).exists():
            curr_user = User.objects.get(username=usrname)
            if curr_user.password == passwrd:
                login_flag = True
                print("Logged in!")
                # return HttpResponseRedirect(reverse('accounts:home'))
                return render(request, 'accounts/home.html', {'login_flag':login_flag})

        else:
            print("Someone tried to login and failed!")
            print("Type: {} Username: {} and password: {}".format(type(usrname),usrname,passwrd))
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request, 'accounts/login.html',{'login_flag':login_flag})