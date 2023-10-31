from django.contrib import admin
from django.contrib import admin
from .models import *

# Register your models here.



@admin.register(Invoice)
class Invoiceadmin(admin.ModelAdmin):
    list_display=["id","title","customer",
"description",
"logo",
"invoice_number",
"invoice_date",
"paymnet_due",
"footer_text",]



@admin.register(Customer)
class Customeradmin(admin.ModelAdmin):
    list_display=["id",
                "name",
                "email",
                "phone",
                "first_name",
                "last_name",
                "saved_cards",
                "balance",
                "account_number",
                "notes",
                "website",
                ]
    





@admin.register(Billing_Address)
class Itemadmin(admin.ModelAdmin):
    list_display=["id","currency",
                "address1",
                "address2",
                "country",
                "city",
                "postal",
                "customer",]



@admin.register(Shipping_Address)
class Itemadmin(admin.ModelAdmin):
    list_display=["id","ship_to",
            "address1",
            "address2",
            "country",
            "city",
            "postal",
            "phone",
            "delivery_instructions",
            "customer",
                ]






@admin.register(Item)
class Itemadmin(admin.ModelAdmin):
    list_display=["id","invoice","name",
                "customer",
                "description",
                "quantity",
                "price",
                "amount",
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
