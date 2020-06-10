from django.db import models
from products.models import Phone
from django.urls import reverse

class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    delivery_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # username = user.username

    def __str__(self):
        return "Cart of %s" % self.user.username

    def get_absolute_url(self):
        return reverse('accounts:account_page', kwargs={'slug':user.username})

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ManyToManyField(Phone,related_name='product_in_cart')

    def __str__(self):
        return "Item in cart: %s " % self.product.name
