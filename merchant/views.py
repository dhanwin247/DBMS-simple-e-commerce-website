from django.shortcuts import render
from . import forms
from merchant.forms import ProductForm
# from products.forms import ProductForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_product(request): 

    new_merchant_form = ProductForm

    registered = False

    if request.method == 'POST':
        new_product_form = ProductForm(data=request.POST)

        if new_product_form.is_valid(): 
            new_product_form.save()
            registered = True

        else:
            print("ERROR FORM INVALID")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:home'))

def merchant_login(request):

    global login_flag 
    global curr_merchant

    if request.method == 'POST': 
        merchant_username = request.POST.get('merchant_username')
        merchant_password = request.POST.get('merchant_password')

        if merchant:
            if merchant.is_active:
                login(request, merchant)
                return HttpResponseRedirect(reverse('accounts:home'))

            else: 
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request, 'accounts/login.html', {})