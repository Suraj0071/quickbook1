from django.contrib import admin
from .models import *

admin.site.register(profile)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ["id",'journal', 'date', 'reference', 'description', 'account', 'account_name', 'debit_amount', 'credit_amount', 'offset_account', 'memo', 'department']



@admin.register(ExpenseCategory)
class ExpenseCategoryadmin(admin.ModelAdmin):
    list_display=["id","name",
                  
    ]

@admin.register(Currency)
class Currencyadmin(admin.ModelAdmin):
    list_display=["id","currency",
    ]