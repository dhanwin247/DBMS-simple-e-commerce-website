from django.contrib import admin
from accounts.models import User,Cart,CartProduct
# Register your models here.
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(CartProduct)
