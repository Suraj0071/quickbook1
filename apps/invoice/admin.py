from django.contrib import admin
from django.contrib import admin
from .models import *

# Register your models here.



@admin.register(Invoice)
class Invoiceadmin(admin.ModelAdmin):
    list_display=["id","title",
"description",
"logo",
"invoice_number",
"invoice_date",
"paymnet_due",
"footer_text",]



@admin.register(Customer)
class Customeradmin(admin.ModelAdmin):
    list_display=["id","invoice",
                "name",
                "email",
                "phone",
                "first_name",
                "last_name",
                ]
    

@admin.register(Item)
class Itemadmin(admin.ModelAdmin):
    list_display=["id","invoice","name",
                "description",
                "quantity",
                "price",
                "amout",
                ]




@admin.register(Business)
class EmailTokenadmin(admin.ModelAdmin):
    list_display=["id","name",
                "address1",
                "address2",
                "city",
                "zip_code",
                "country",
                "state",
                "phone",
                "fax",
                "mobile",
                "toll_free",
                "website",
                "invoice",]
