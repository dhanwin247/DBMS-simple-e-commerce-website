from django.shortcuts import render
from . import forms
from app1.models import User

# Create your views here.
def home(request):
    return render(request,'app1/home.html')

def login(request):
    return render(request,'app1/login.html')

def about(request):
    return render(request,'app1/about.html')

def signup(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        curr_user = User()
        form = forms.SignupForm(request.POST)
        #

    return render(request,'app1/signup.html',{'form':form})

def signup_new(request):
    if request.method == 'POST':
        new_user = User()
        new_user.username = request.POST.get('username')
        new_user.password = request.POST.get('user_password')
        new_user.email = request.POST.get('user_email')
        new_user.first_name = request.POST.get('first_name')
        new_user.last_name = request.POST.get('last_name')
        new_user.delivery_address = request.POST.get('delivery_address')
        new_user.phone_number = request.POST.get('phone_number')

        # print(new_user)

        new_user.save()

    return render(request, 'app1/signup_new.html')

