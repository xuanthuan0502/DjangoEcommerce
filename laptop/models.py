from unicodedata import name
from django.db import models
from numpy import require
from django.contrib.auth.models import User
from product.models import Product
class Laptop(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    ram = models.CharField(max_length=200,null= True,blank=True)
    cpu = models.CharField(max_length=200,null= True,blank=True)
    camera = models.CharField(max_length=200,null= True,blank=True)
    audio = models.CharField(max_length=200,null= True,blank=True)
    keyboard = models.CharField(max_length=200,null= True,blank=True)
    communications_network = models.CharField(max_length=200,null= True,blank=True)
    enternal_port = models.CharField(max_length=200,null= True,blank=True)
    ac_acdopted = models.CharField(max_length=200,null= True,blank=True)
    battery = models.CharField(max_length=200,null= True,blank=True)
    vga = models.CharField(max_length=200,null= True,blank=True)
    screen = models.CharField(max_length=200,null= True,blank=True)  
    color = models.CharField(max_length=200,null= True,blank=True)  
    
    #pub_date = models.DateTimeField('date published')
    def __str__(self):
        return f"{self.name}-{self.code}"



