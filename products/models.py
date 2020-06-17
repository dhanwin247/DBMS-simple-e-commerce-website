from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=200, unique=True) #the phone model name
    color = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    storage = models.PositiveIntegerField()
    camera = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    processor = models.CharField(max_length=100)
    ram = models.PositiveIntegerField()
    picture = models.ImageField(upload_to='phone_pics', blank=True) #A phone may not need an associated picture; but blank can be set to false later
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
