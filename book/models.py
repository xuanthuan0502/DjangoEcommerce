from unicodedata import name
from django.db import models
from numpy import require
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from product.models import Product

class Book(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200,null= True,blank=True)
    author = models.CharField(max_length=200,null= True,blank=True)
    publishedhouse = models.CharField(max_length=200,null= True,blank=True)
   # publishedyear = models.DateTimeField( default = True)
    publishedyear = models.DateField(null= True,blank=True)
    language = models.CharField(max_length=200,null= True,blank=True)
    
    #pub_date = models.DateTimeField('date published')
    def __str__(self):
        return f"{self.title,self.product}"
  #  def was_published_recently(self):
   #     return self.publishedyear >= timezone.now() - datetime.timedelta(days=1)
    