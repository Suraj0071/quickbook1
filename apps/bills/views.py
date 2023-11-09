from django.shortcuts import render, redirect
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
        vendor = Vendor.objects.all()
        context = {
            "vendor":vendor
        }
        
        return render(request, "vendors.html",context)



class VendorCreate(View):
    def get(self, request):
        currency = Currency.objects.all()
        context = {
            "currency":currency
        }
        return render(request, "vendors_add.html",context)
    
    def post(self,request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        currency = request.POST.get("currency")
        
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        city = request.POST.get("city")
        postal = request.POST.get("postal")
        phone = request.POST.get("phone")
        obj = Vendor.objects.create(name=name, email=email,currency_id=currency,address1=address1,address2=address2,
                                    city=city,postal=postal,phone=phone,)

        return redirect("vendors")
        


class VendorEdit(View):
    def get(self, request,id):
        response = Vendor.objects.get(id=id)
        currency   = Currency.objects.all()
        context = {
            "response" :response ,
            "currency"    :currency
        }

        return render(request, "vendors_edit.html",context)
    def post(self,request,id):
        response = Vendor.objects.get(id=id)
        response.name = request.POST.get("name")
        response.email = request.POST.get("email")
        response.currency_id = request.POST.get("currency")
        response.address1 = request.POST.get("address1")
        response.address2 = request.POST.get("address2")
        response.city = request.POST.get("city")
        response.postal = request.POST.get("postal")
        response.phone = request.POST.get("phone")
        response.save()
        return redirect("vendors")
    


def vendor_delete(request,id):
    print("This is  vill rin ")
    obj = Vendor.objects.get(id=id)
    obj.delete()
    return redirect("vendors")

    