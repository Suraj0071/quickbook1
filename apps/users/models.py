from django.db import models
from django.contrib.auth.models import User
from datetime import date



class Currency(models.Model):
    currency  = models.CharField(max_length=200)
    def __str__(self):
        return self.currency

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name




class profile(models.Model):
    '''a model for a blog post'''
    Name = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone_no = models.CharField(max_length=100)
    Email = models.TextField()

    def __str__(self):
        staff_status = "-(staff user)" if self.is_staff else " "
        return f"{self.username}  {staff_status}"
    




class  File(models.Model):
    file  = models.FileField(null=True,blank=True)
    journal = models.CharField(max_length=100,null=True,blank=True)
    date  =models.CharField(max_length=100,null=True,blank=True)
    reference =models.CharField(max_length=100,null=True,blank=True)
    description  = models.CharField(max_length=100,null=True,blank=True)
    account  = models.CharField(max_length=100,null=True,blank=True)
    account_name = models.CharField(max_length=100,null=True,blank=True)
    debit_amount = models.CharField(max_length=100,null=True,blank=True)
    credit_amount=models.CharField(max_length=100,null=True,blank=True)
    offset_account =models.CharField(max_length=100,null=True,blank=True)
    memo          =models.CharField(max_length=100,null=True,blank=True)
    department =models.CharField(max_length=100,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)






class EmailToken(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="email_user",
        blank=True,
        null=True,
    )
    email_token = models.CharField(max_length=50)