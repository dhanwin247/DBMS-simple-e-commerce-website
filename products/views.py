from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from . import models
# Create your views here.

class ProductHomeView(TemplateView):
    template_name = 'products/product_base.html'

class ProductListView(ListView):
    model = models.Phone
    template_name = 'products/product_list.html'

class ProductDetailView(DetailView):
    context_object_name = 'product_details'
    model = models.Phone
    template_name = 'products/product_details.html'
