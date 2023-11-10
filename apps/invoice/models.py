from django.db import models

# Create your models here.
from django.contrib.auth.models import User




class Tax(models.Model):
    abbreviation =  models.CharField(max_length=200)
    tax_rate  = models.CharField(max_length=200)
    description  = models.TextField(null=True,blank=True)
    tax_num    = models.BooleanField(default=False)
    show_tax_number_on_invoices =models.BooleanField(default=False)
    is_this_tax_recoverable   =models.BooleanField(default=False)
    is_this_a_compound_tax  =models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.abbreviation



class Customer(models.Model):
    name =  models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    saved_cards  = models.CharField(max_length=100,null=True,blank=True)
    balance     = models.CharField(max_length=100,null=True,blank=True)
    account_number = models.CharField(max_length=100,null=True,blank=True)
    notes = models.TextField(null=True,blank=True)
    website  = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True,default="Invoice")
    description = models.TextField(null=True,blank=True)
    pos_so_no  = models.TextField(null=True,blank=True)
    logo = models.ImageField(upload_to="static/images",null=True,blank=True)
    invoice_number = models.CharField(max_length=100,null=True,)
    invoice_date = models.DateField()
    paymnet_due = models.DateField()
    footer_text = models.TextField(null=True,blank=True)
    is_draft = models.BooleanField(default=True)
    is_send = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)  

    def __str__(self) -> str:
        return self.title  



class Item(models.Model):
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    amount = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True) 

    def __str__(self) -> str:
        return self.name  
   



class Business(models.Model):
    name = models.CharField(max_length=100)
    address1 =  models.CharField(max_length=100,null=True,blank=True)
    address2  =  models.CharField(max_length=100,null=True,blank=True)
    city     =  models.CharField(max_length=100,null=True,blank=True)
    zip_code =  models.CharField(max_length=100,null=True,blank=True)
    country  =  models.CharField(max_length=100,null=True,blank=True)
    state     =  models.CharField(max_length=100,null=True,blank=True)
    phone   =  models.CharField(max_length=100,null=True,blank=True)
    fax      =  models.CharField(max_length=100,null=True,blank=True)
    mobile   =  models.CharField(max_length=100,null=True,blank=True)
    toll_free =  models.CharField(max_length=100,null=True,blank=True)
    website =  models.CharField(max_length=100,null=True,blank=True)
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.name


class Billing_Address(models.Model):
    currency  =  models.CharField(max_length=100,null=True,blank=True)
    address1 =  models.CharField(max_length=100,null=True,blank=True)
    address2  =  models.CharField(max_length=100,null=True,blank=True)
    country  =  models.CharField(max_length=100,null=True,blank=True)
    city =  models.CharField(max_length=100,null=True,blank=True)
    postal  =  models.CharField(max_length=100,null=True,blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self) -> str:
        return self.address1  



class Shipping_Address(models.Model):
    ship_to  = models.CharField(max_length=100,null=True,blank=True)
    address1 =  models.CharField(max_length=100,null=True,blank=True)
    address2  =  models.CharField(max_length=100,null=True,blank=True)
    country  =  models.CharField(max_length=100,null=True,blank=True)
    city =  models.CharField(max_length=100,null=True,blank=True)
    postal  =  models.CharField(max_length=100,null=True,blank=True)
    phone =  models.CharField(max_length=100,null=True,blank=True)
    delivery_instructions =  models.CharField(max_length=100,null=True,blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self) -> str:
        return self.ship_to  


    


class Product_Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    price = models.CharField(max_length=200,null=True,blank=True)
    buy_this = models.BooleanField(default=False)
    sell_this = models.BooleanField(default=False)
    income_account = models.CharField(max_length=100,null=True,blank=True)
    expense_account  =models.CharField(max_length=100,null=True,blank=True)
    sales_tax   =  models.ForeignKey(Tax,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self) -> str:
        return self.name  


    
