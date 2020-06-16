from django.contrib import admin
from accounts.models import User,Cart,CartProduct,Purchase,PurchaseProduct
# Register your models here.
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Purchase)
admin.site.register(PurchaseProduct)
