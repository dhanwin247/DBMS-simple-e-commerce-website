from django.urls import path
from merchant import views

#TEMPLATE URLS
app_name = 'merchant'

urlpatterns = [
    path('',views.merchant_login, name='merchant_login'),
    path('register',views.register_product, name='register_product'),
    path('home/',views.home, name='home'),
    path('user_login/',views.user_login, name='user_login'),
    # path('logout/',views.user_logout,name='logout')
    path('about/',views.about, name='about'),
]
