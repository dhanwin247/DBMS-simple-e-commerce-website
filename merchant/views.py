from django.shortcuts import render
from . import forms
from merchant.forms import ProductForm
from merchant.models import Merchant

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

login_flag = False
curr_merchant = None

# Create your views here.
def register_product(request): 

    global login_flag
    global curr_merchant

    new_product_form = ProductForm

    registered = False

    if request.method == 'POST':
        new_product_form = ProductForm(request.POST, request.FILES)

        if new_product_form.is_valid(): 
            # current_product = new_product_form.save()
            new_product_form.save()
            registered = True
            # print("form valid but pic not found :(")

            # if 'picture' in request.FILES:
            #     print("found picture")
            #     current_product.picture = request.FILES['picture']

            # current_product.save()

        else:
            print("ERROR FORM INVALID")

    return render(request, 'merchant/register.html', {'form':new_product_form, 'login_flag':login_flag})

def merchant_logout(request):

    global curr_merchant
    global login_flag

    login_flag = False
    curr_merchant = None
    return HttpResponseRedirect(reverse('merchant:merchant_login'))

def merchant_login(request):

    global login_flag
    global curr_merchant

    if request.method == 'POST': 
        merchant_usrname = request.POST.get('merchant_username')
        merchant_passwrd = request.POST.get('merchant_password')

        if Merchant.objects.filter(merchant_username=merchant_usrname).exists() and Merchant.objects.get(merchant_username=merchant_usrname).merchant_password == merchant_passwrd:
            print("Merchant Logged in!")
            login_flag = True
            curr_merchant = merchant_usrname
            print("Current Merchant is " + curr_merchant)
            return HttpResponseRedirect(reverse('merchant:register_product'))

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password: {}".format(merchant_usrname,merchant_passwrd))
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request, 'merchant/register.html', {'login_flag':login_flag})