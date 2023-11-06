from django.db import models

# Create your models here.




class Vendor(models.Model):
    name = models.CharField(max_length=200)



class ExpenseCategory(models.Model):
    name = models.CharField(max_length=200)


class Currency(models.Model):
    currency  = models.CharField(max_length=200)



class Bills(models.Model):
    vandor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    bill_date    = models.DateField()
    due_date = models.DateField()
    bill_number = models.CharField(max_length=200)
    po_so_no     = models.CharField(max_length=200)
    notes      = models.TextField(null=True ,blank=True)
    expence = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
