from django.db import models

# Create your models here.
class contact(models.Model):  
    name = models.CharField(max_length=111)
    email = models.EmailField()
    address = models.CharField(max_length=15)  
    phno = models.IntegerField() 

class medicine(models.Model):
    prodName=models.CharField(max_length=510)
    prodDescription=models.CharField(max_length=515)
    prodImage=models.CharField(max_length=515)
    prodPrice=models.IntegerField()

class order(models.Model):
    orderName=models.CharField(max_length=510)
    orderaddress=models.CharField(max_length=515)
    orderemail=models.CharField(max_length=515)
    orderphone=models.IntegerField()
    items=models.CharField(max_length=44)
    price=models.IntegerField()
    quantity=models.IntegerField()
    delivery=models.BooleanField(default=False)
    
