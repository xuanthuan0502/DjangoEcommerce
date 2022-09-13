from unicodedata import name
from django.db import models
from numpy import require
from django.contrib.auth.models import User
from rest_framework import serializers
from product.models import Product
class MobilePhone(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE,primary_key=True)
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    ram = models.CharField(max_length=200,null= True,blank=True)
    cpu = models.CharField(max_length=200,null= True,blank=True)
    camera = models.CharField(max_length=200,null= True,blank=True)
    audio = models.CharField(max_length=200,null= True,blank=True)
    screen_size = models.CharField(max_length=200,null= True,blank=True)
    display = models.CharField(max_length=200,null= True,blank=True)
    Sim = models.CharField(max_length=200,null= True,blank=True)
    GPS = models.CharField(max_length=200,null= True,blank=True)
    enternal_ports = models.CharField(max_length=200,null= True,blank=True)
    battery = models.CharField(max_length=200,null= True,blank=True)
    wifi = models.CharField(max_length=200,null= True,blank=True)  
    color = models.CharField(max_length=200,null= True,blank=True)  
    
    #pub_date = models.DateTimeField('date published')
    def __str__(self):
        return f"{self.name}-{self.code}"

