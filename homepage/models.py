from django.db import models

# Create your models here.

class Product(models.Model):
    price=models.DecimalField(decimal_places=5,max_digits=15)
    description=models.JSONField()
    name=models.CharField(max_length=500)
    img=models.ImageField()
    sellerid=models.IntegerField(default=0)
    productid=models.IntegerField(default=0)

class Users(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    wishlist=models.JSONField(default=dict)