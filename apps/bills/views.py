from django.shortcuts import render
from django.views import View
from . models import *
# Create your views here.

class BillsView(View):
    def get(self, request):
        vendor = Vendor.objects.all()
        context = {
            "vendor" : vendor
        }
        return render(request, "bills.html",context)
    

class CreateBill(View):
    def get(self, request):
        return render(request, "bills_add.html",)


class EditBill(View):
    def get(self, request):
        return render(request, "bills_edit.html",)
    
