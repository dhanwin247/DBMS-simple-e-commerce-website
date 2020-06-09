from django.db import models

# Create your models here.
class Merchant(models.Model):
    merchant_name = models.CharField(max_length=200, unique=True)
    merchant_email = models.CharField(max_length=200)
    merchant_username = models.CharField(max_length=200)
    merchant_password = models.CharField(max_length=200)

    def __str__(self):
        return self.merchant_name