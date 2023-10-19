from django.db import models

# Create your models here.



class Invoice(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True,default="Invoice")
    description = models.TextField(null=True,blank=True)
    logo = models.ImageField(upload_to="static/images",null=True,blank=True)
    invoice_number = models.CharField(max_length=100)
    invoice_date = models.DateField()
    paymnet_due = models.DateField()
    footer_text = models.TextField(null=True,blank=True)
    is_draft = models.BooleanField(default=True)
    is_send = models.BooleanField(default=True)


class Customer(models.Model):
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    

class Item(models.Model):
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    amout = models.IntegerField()    



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
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)



