from unicodedata import name
from django.db import models
from numpy import quantile, require
from django.contrib.auth.models import User
from django.utils import timezone
from customer.models import Customer
import datetime


class Product(models.Model):
    
    name = models.CharField(max_length=200)
    price = models.FloatField(null= True,blank=True)
    img = models.ImageField(upload_to ='images',max_length=200,null= True,default = None)
    choice = {
        ('mobilephone','mobilephone'),
        ('laptop','laptop'),
        ('book','book'),
    }
    category = models.CharField(max_length=200,null= True,blank=True,choices=choice)
    #pub_date = models.DateTimeField('date published')
    def __str__(self):
        return f"{self.name}"
  #  def was_published_recently(self):
   #     return self.publishedyear >= timezone.now() - datetime.timedelta(days=1)

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null= True,blank=True)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(null= True,blank=True)
    status = models.BooleanField (default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    def register(self):
        self.save()
    def get_total(self):
        return self.price*self.quantity

class Payment(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200,null= True,blank=True)
    tax = models.FloatField(null= True,blank=True)
    def register(self):
        self.save()

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null= True,blank=True)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,null= True,blank=True)
    
    price = models.FloatField(null= True,blank=True)
    status = models.BooleanField (default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    def register(self):
        self.save()

class Shipment(models.Model):
    
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null= True,blank=True)
    name = models.CharField(max_length=200,null= True,blank=True)
    phone = models.CharField(max_length=200,null= True,blank=True)
    email = models.CharField(max_length=200,null= True,blank=True)
    address = models.CharField(max_length=200,null= True,blank=True)
    
    def register(self):
        self.save()

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null= True,blank=True)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(null= True,blank=True)
    def register(self):
        self.save()