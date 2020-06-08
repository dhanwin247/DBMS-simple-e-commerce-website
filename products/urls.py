from django.urls import path
from products import views

#TEMPLATE URLS
app_name = 'products'

urlpatterns = [
    path('',views.ProductHomeView.as_view()),
    path('list/',views.ProductListView.as_view(),name='list'),#some mistake
]
