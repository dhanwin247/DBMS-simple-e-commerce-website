from django.urls import path
from accounts import views

#TEMPLATE URLS
app_name = 'accounts'

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('home/',views.home, name='home'),
    path('user_login/',views.user_login, name='user_login'),
    path('logout/',views.user_logout,name='logout'),
    path('about/',views.about, name='about'),
    path('accounts/',views.account_page_view, name='account_page'),
    path('accounts/product_add/',views.add_quantity,name='product_add'),
    path('accounts/product_subtract/',views.subtract_quantity,name='product_subtract'),
    path('accounts/purchase/',views.purchase_page_view, name='purchase_page')
]
