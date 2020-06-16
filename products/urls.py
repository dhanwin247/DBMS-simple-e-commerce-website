from django.urls import path
from products import views

#TEMPLATE URLS
app_name = 'products'

urlpatterns = [
    path('',views.product_home_view,name='prodhome'),
    path('list/',views.product_list_view,name='prodlist'),
    path('list/<product_id>/',views.product_detail_view,name='proddetail'),
]
