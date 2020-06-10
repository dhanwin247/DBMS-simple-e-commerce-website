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

# def login(request):
#     return render(request,'accounts/login.html')

def about(request):
    return render(request,'accounts/about.html', {'login_flag':login_flag})




# @login_required
def user_logout(request):

    global curr_user
    # logout(request)
    global login_flag

    login_flag = False
    print(curr_user + "logged out")
    curr_user = None
    # print("current user is " + curr_user)
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
            curr_user = usrname

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
            # curr_user = User.objects.get(username=usrname)
            # if curr_user.password == passwrd:
            print("Logged in!")
            login_flag = True
            curr_user = usrname
            print("Current User is " + curr_user)
            # return HttpResponseRedirect(reverse('accounts:home'))
            return render(request, 'accounts/home.html', {'login_flag':login_flag})

        else:
            print("Someone tried to login and failed!")
            print("Type: {} Username: {} and password: {}".format(type(usrname),usrname,passwrd))
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request, 'accounts/login.html',{'login_flag':login_flag})

def account_page_view(request):
    return render(request, 'accounts/account_base.html')
    # if Cart.objects.filter(user.username=curr_user).exists():
    #     curr_cart = Cart.objects.get(user.username=curr_user)
    #     curr_cart_product = CartProduct.objects.get(cart=curr_cart)
    #     return render(request, 'accounts/account_page.html',{'cart':curr_cart, 'cart_products':curr_cart_product})
