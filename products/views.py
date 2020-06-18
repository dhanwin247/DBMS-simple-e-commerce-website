from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from accounts.views import curr_user_object
from accounts import views
from accounts.models import CartProduct, Cart
from . import models
# Create your views here.
phone=None

def product_list_view(request):
    curr_user_object = views.curr_user_find()
    all_products = models.Phone.objects.all()
    phone_matrix = []
    curr_list = []
    for phone in all_products:
        if len(curr_list) == 3:
            phone_matrix.append(curr_list)
            curr_list = []
        curr_list.append(phone)
    if curr_list:
        phone_matrix.append(curr_list)

    if request.GET.get('Add to cart!') == 'Add to cart!':
        curr_cart = Cart.objects.get(user=curr_user_object)
        if not CartProduct.objects.filter(cart=curr_cart, product=phone).exists():
            print("the current user is {}".format(curr_user_object.username))
            # curr_cart = Cart.objects.get(user=curr_user_object)
            cart_product = CartProduct(cart=curr_cart,product=phone,quantity=1)
            cart_product.save()
        else:
            print( )
    return render(request,'products/product_list.html',{'phone_matrix':phone_matrix})

def product_detail_view(request,product_id):
    global phone
    phone = models.Phone.objects.get(pk=product_id)
    
    MRP = phone.price
    if phone.brand == 'Apple':
        MRP = phone.price * 1.3
    elif phone.brand == 'Samsung':
        MRP = phone.price * 1.2
    else:
        MRP = phone.price * 1.1

    return render(request,'products/product_details.html',{'phone':phone, 'MRP':MRP})
