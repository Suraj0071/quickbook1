from django.db import models
from apps.invoice.models import Item , Tax ,Product_Service

# Create your models here.




class ExpenseCategory(models.Model):
    name = models.CharField(max_length=200)


class Currency(models.Model):
    currency  = models.CharField(max_length=200)





class Vendor(models.Model):
    name = models.CharField(max_length=200)
    email  = models.EmailField(null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE , null=True, blank=True)
    address1 =  models.CharField(max_length=100,null=True,blank=True)
    address2  =  models.CharField(max_length=100,null=True,blank=True)
    city =  models.CharField(max_length=100,null=True,blank=True)
    postal  =  models.CharField(max_length=100,null=True,blank=True)
    phone =  models.CharField(max_length=100,null=True,blank=True)

  

class Bills(models.Model):
    vandor = models.ForeignKey(Vendor, on_delete=models.CASCADE,null=True, blank=True)
    status = models.BooleanField(default=False)
    bill_date    = models.DateField()
    due_date = models.DateField()
    bill_number = models.CharField(max_length=200)
    po_so_no     = models.CharField(max_length=200)
    notes      = models.TextField(null=True ,blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    



class  Bills_item(models.Model):
    description = models.TextField(null=True ,blank=True)
    quantity  = models.CharField(max_length=200,null=True ,blank=True)
    price   =  models.CharField(max_length=50,null=True ,blank=True)
    product =  models.ForeignKey(Product_Service,on_delete=models.CASCADE,null=True, blank=True) 
    expence = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    tax   = models.ForeignKey(Tax,on_delete=models.CASCADE,null=True, blank=True) 
    bills = models.ForeignKey(Bills,on_delete=models.CASCADE,null=True, blank=True) 