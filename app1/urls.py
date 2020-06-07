from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('signup_new/', views.signup_new, name='signup_new'),
    path('signup2/', views.signup2, name='signup2'),
    path('home/',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('about/',views.about, name='about')
]
