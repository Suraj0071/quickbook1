from django.shortcuts import render
from django.views import View
from . models import *
# Create your views here.

from apps.invoice.models import Product_Service ,Tax
class BillsView(View):
    def get(self, request):
        vendor = Vendor.objects.all()
        context = {
            "vendor" : vendor
        }
        return render(request, "bills.html",context)
    

class CreateBill(View):
    def get(self, request):
        vendor = Vendor.objects.all()
        currency = Currency.objects.all()
        expence = ExpenseCategory.objects.all()
        product   = Product_Service.objects.all()
        tax     = Tax.objects.all()

        print(currency)
        context = {
            "vendor" : vendor,
            "currency" :currency,
            "expence" :expence,
            "product"   : product,
            "tax"   : tax
        }
        return render(request, "bills_add.html",context)
    
    def post(self,request):
        venndor  = request.POST.get("venndor")
        currency  = request.POST.get("currency")
        bill_date  = request.POST.get("bill_date")
        due_date  = request.POST.get("due_date")
        po_so_no  = request.POST.get("po_so_no")
        bill_number  = request.POST.get("bill_number")
        notes  = request.POST.get("notes")
        expence  = request.POST.get("expence")
        description  = request.POST.get("description")
        quantity  = request.POST.getlist("quantity")
        quantity  = request.POST.getlist("e")






class EditBill(View):
    def get(self, request):
        return render(request, "bills_edit.html",)
    


class VendorsView(View):
    def get(self, request):
        
        return render(request, "vendors.html",)



class VendorCreate(View):
    def get(self, request):
        currency = Currency.objects.all()
        context = {
            "currency":currency

        }
        
        return render(request, "vendors_add.html",context)
    
    def post(self,request):
        pass
      


class VendorEdit(View):
    def get(self, request):
        return render(request, "vendors_edit.html",)
    