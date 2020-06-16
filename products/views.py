from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from accounts import views
from accounts.models import CartProduct, Cart
from . import models
# Create your views here.
phone=None
# class ProductHomeView(TemplateView):
#     template_name = 'products/product_base.html'

def product_home_view(request):
    return render(request,'products/product_base.html')
#
# class ProductListView(ListView):
#     model = models.Phone
#     template_name = 'products/product_list.html'

def product_list_view(request):
    all_products = models.Phone.objects.all()
    return render(request,'products/product_list.html',{'all_products':all_products})

# class ProductDetailView(DetailView):
#     context_object_name = 'product_details'
#     model = models.Phone
#     template_name = 'products/product_details.html'

def product_detail_view(request,product_id):
    global phone
    phone = models.Phone.objects.get(pk=product_id)
    return render(request,'products/product_details.html',{'phone':phone})

def add_to_cart():
    global phone
    curr_user = views.curr_user_find()
    curr_cart = Cart.objects.get(user=curruser)
    cart_product = CartProduct(cart=curr_cart,product=phone)
    cart_product.save()
