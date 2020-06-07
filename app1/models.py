from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    userid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    delivery_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
