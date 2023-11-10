from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Vendor)
class Vendoradmin(admin.ModelAdmin):
    list_display=["id","name",
    ]

@admin.register(ExpenseCategory)
class ExpenseCategoryadmin(admin.ModelAdmin):
    list_display=["id","name",
                  
    ]

@admin.register(Currency)
class Currencyadmin(admin.ModelAdmin):
    list_display=["id","currency",
    ]


@admin.register(Bills)
class Billsadmin(admin.ModelAdmin):
    list_display=["id",
            "vandor",
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


