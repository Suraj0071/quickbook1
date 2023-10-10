from django.contrib import admin
from .models import profile,File,EmailToken

admin.site.register(profile)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ["id",'journal', 'date', 'reference', 'description', 'account', 'account_name', 'debit_amount', 'credit_amount', 'offset_account', 'memo', 'department']




@admin.register(EmailToken)
class EmailTokenadmin(admin.ModelAdmin):
    list_display=['id',"user","email_token"]