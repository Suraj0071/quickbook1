from django.db import models
from apps.invoice.models import  Tax ,Product_Service
from apps.users.models import Currency,ExpenseCategory

# Create your models here.









class Vendor(models.Model):
    name = models.CharField(max_length=200)
    email  = models.EmailField(null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE , null=True, blank=True)
    address1 =  models.CharField(max_length=100,null=True,blank=True)
    address2  =  models.CharField(max_length=100,null=True,blank=True)
    city =  models.CharField(max_length=100,null=True,blank=True)
    postal  =  models.CharField(max_length=100,null=True,blank=True)
    phone =  models.CharField(max_length=100,null=True,blank=True)

    # def __str__(self):
    #     return self.name

  

class Bills(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,null=True, blank=True)
    status = models.BooleanField(default=False)
    bill_date    = models.DateField()
    due_date = models.DateField()
    bill_number = models.CharField(max_length=200)
    po_so_no     = models.CharField(max_length=200)
    notes      = models.TextField(null=True ,blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)


   


class  Bills_item(models.Model):
    description = models.TextField(default="")
    quantity  = models.CharField(max_length=200,null=True ,blank=True)
    price   =  models.CharField(max_length=50,null=True ,blank=True)
    product =  models.ForeignKey(Product_Service,on_delete=models.CASCADE,null=True, blank=True) 
    expence = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    tax   = models.ForeignKey(Tax,on_delete=models.CASCADE,null=True, blank=True) 
    bills = models.ForeignKey(Bills,on_delete=models.CASCADE,null=True, blank=True) 
