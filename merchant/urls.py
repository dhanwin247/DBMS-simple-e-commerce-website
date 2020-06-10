from django.urls import path
from merchant import views as account_views
from accounts import views

#TEMPLATE URLS
app_name = 'merchant'

urlpatterns = [
    path('',views.merchant_login, name='merchant_login'),
    path('register',views.register_product, name='register_product'),
    path('home/',account_views.home, name='home'),
    path('merchant_login/',views.merchant_login, name='merchant_login'),
    # path('logout/',views.user_logout,name='logout')
    path('about/',account_views.about, name='about'),
]
