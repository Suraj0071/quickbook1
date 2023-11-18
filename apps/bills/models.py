from django.db import models
from apps.invoice.models import  Tax ,Product_Service
from apps.users.models import Currency,ExpenseCategory
from enum import Enum


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


#dont'change this give import error


class PaymentMothod(Enum):
    Bank_payment = "Bank payment"
    Cash         = "Cash"
    Cheque         = "Cheque"
    Credit_card   = "Credit_card"
    PayPal         = "PayPal"
    Others         = "Others"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class Record_Payment(models.Model):
    payment_method = models.CharField(max_length=100,choices=PaymentMothod.choices())
    amount = models.CharField(max_length=200,null=True, blank=True)
    payment_date = models.DateField(null=True,blank=True)
    payment_account = models.CharField(max_length=200,null=True, blank=True)
    notes           = models.TextField(null=True,blank=True)
  

class Bills(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,null=True, blank=True)
    status = models.BooleanField(default=False)
    bill_date    = models.DateField()
    due_date = models.DateField()
    bill_number = models.CharField(max_length=200)
    po_so_no     = models.CharField(max_length=200)
    notes      = models.TextField(null=True ,blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.ForeignKey(Record_Payment,on_delete=models.CASCADE,null=True, blank=True)


   


class  Bills_item(models.Model):
    description = models.TextField(default="")
    quantity  = models.CharField(max_length=200,null=True ,blank=True)
    price   =  models.CharField(max_length=50,null=True ,blank=True)
    product =  models.ForeignKey(Product_Service,on_delete=models.CASCADE,null=True, blank=True) 
    expence = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    tax   = models.ForeignKey(Tax,on_delete=models.CASCADE,null=True, blank=True) 
    bills = models.ForeignKey(Bills,on_delete=models.CASCADE,null=True, blank=True) 






 
