from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def login(request):
    return render(request,'app1/login.html')

def about(request):
    return render(request,'about/about.html')

def signup(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        #
    return render(request,'app1/signup.html',{'form':form})
