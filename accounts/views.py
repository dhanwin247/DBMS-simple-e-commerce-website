from django.shortcuts import render
from accounts.models import User
from accounts.forms import SignupForm
from django.contrib.auth.hashers import make_password

from django.views.generic.detail import DetailView
from accounts.models import User, Cart, CartProduct
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

login_flag = False
curr_user = None

# Create your views here.
def home(request):
    return render(request,'accounts/home.html', {'login_flag':login_flag})


def about(request):
    return render(request,'accounts/about.html', {'login_flag':login_flag})


def user_logout(request):
    global curr_user
    global login_flag

    login_flag = False
    curr_user = None

    return HttpResponseRedirect(reverse('accounts:home'))


def signup(request):
    global login_flag
    global curr_user

    user_form = SignupForm

    registered = False

    if request.method == 'POST':
        user_form = SignupForm(data=request.POST)

        if user_form.is_valid():
            curr_user_form = user_form.save()

            registered = True
            login_flag = True
            curr_user = curr_user_form.username

            # return HttpResponseRedirect(reverse('accounts:home'))
            return render(request, 'accounts/home.html', {'login_flag':login_flag})

        else:
            print('user_form.errors')

    return render(request, 'accounts/signup.html', {'form':user_form, 'registered':registered})


def user_login(request):
    global login_flag
    global curr_user

    if request.method == 'POST':
        usrname = request.POST.get('username')
        passwrd = request.POST.get('password')

        if User.objects.filter(username=usrname).exists() and User.objects.get(username=usrname).password == passwrd:
            print("Logged in!")
            login_flag = True
            curr_user = usrname
            print("Current User is " + curr_user)

            return render(request, 'accounts/home.html', {'login_flag':login_flag})

        else:
            print("Someone tried to login and failed!")
            print("Type: {} Username: {} and password: {}".format(type(usrname),usrname,passwrd))
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request, 'accounts/login.html',{'login_flag':login_flag})

def curr_user_find():
    global curr_user

    current_user = User.objects.get(username=curr_user)
    return current_user

def account_page_view(request):
    global curr_user 

    curruser = User.objects.get(username=curr_user)
    if Cart.objects.filter(user=curruser).exists():
        curr_cart = Cart.objects.get(user=curruser)
        curr_cart_product=[]
        curr_cart_product = CartProduct.objects.filter(cart=curr_cart)
        for product in curr_cart_product:
            print(product)
        return render(request, 'accounts/account_page.html',{'cart':curr_cart, 'cart_products':curr_cart_product})

    else:
        return HttpResponse("Your cart is empty")
