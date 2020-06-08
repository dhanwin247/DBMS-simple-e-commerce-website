from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from . import models
# Create your views here.

class ProductHomeView(TemplateView):
    template_name = 'products/product_base.html'
    
class ProductListView(ListView):
    model = models.Phone

class ProductDetailView(DetailView):
    context_object_name = 'product_details'
    model = models.Phone
    template_name = 'products/product_details.html'
