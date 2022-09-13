from unicodedata import name
from django.db import models
from numpy import require
from django.contrib.auth.models import User
from product.models import Product


class Clothes(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    size = models.CharField(max_length=200,null= True,blank=True)
    color = models.CharField(max_length=200,null= True,blank=True)
    material = models.CharField(max_length=200,null= True,blank=True)
    sex = models.CharField(max_length=200,null= True,blank=True)
    brand = models.CharField(max_length=200,null= True,blank=True)
    price = models.FloatField(null=True )
    #pub_date = models.DateTimeField('date published')
    def __str__(self):
        return f"{self.type}"