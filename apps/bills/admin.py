from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Vendor)
class Vendoradmin(admin.ModelAdmin):
    list_display=["id","name",
    ]




@admin.register(Bills)
class Billsadmin(admin.ModelAdmin):
    list_display=["id",
            "vendor",
            "status",
            "bill_date",
            "due_date",
            "bill_number",
            "po_so_no",
            "notes",
            "currency",
    ]



@admin.register(Bills_item)
class Bills_itemadmin(admin.ModelAdmin):
    list_display=["id",
                  "description",
                "quantity",
                "price",
                "product",
                "expence",
                "tax",
                "bills",
    ]


