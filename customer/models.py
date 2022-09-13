from django.db import models

# Create your models here.
class Customer(models.Model):
    
    name = models.CharField(max_length=200)
    loginname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200,null= True,blank=True)
    phone = models.CharField(max_length=200,null= True,blank=True)
    #pub_date = models.DateTimeField('date published')
    def __str__(self):
        return f"{self.name}"

    def register(self):
        self.save()    