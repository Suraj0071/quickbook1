from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views import View
from . models import *
from apps.bills.utils import bill_items
# Create your views here.
from django.core.paginator import Paginator

from apps.invoice.models import Product_Service ,Tax


from django.contrib import messages
import pandas as pd
import os
class BillsView(View):
    def get(self, request):
        vendor = Vendor.objects.all()
        bills = Bills.objects.all()
        paginator = Paginator(bills,8)
        pagenumber =request.GET.get('page')
        bills= paginator.get_page(pagenumber)

        context = {
            "vendor" : vendor,
            "bills"  :bills
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
        try:
            venndor  = request.POST.get("venndor")
            currency  = request.POST.get("currency")
            bill_date  = request.POST.get("bill_date")
            due_date  = request.POST.get("due_date")
            po_so_no  = request.POST.get("po_so_no")
            bill_number  = request.POST.get("bill_number")
            notes  = request.POST.get("notes")
            product  = request.POST.getlist("product")
            expence  = request.POST.getlist("expence")
            description  = request.POST.getlist("description")
            quantity  = request.POST.getlist("quantity")
            price  = request.POST.getlist("price")
            tax  = request.POST.getlist("tax")

            obj = Bills.objects.create(vandor_id = venndor, currency_id=currency, bill_date=bill_date,due_date=due_date,bill_number=bill_number,
                                    po_so_no=po_so_no,notes=notes)
            bill_items(obj,product, expence, description, quantity, price, tax)
            return redirect("bills")
        except Exception as e:
            print("This is  exceptiopn",e)
            return  redirect("add-vendors")
         



class EditBill(View):
    def get(self, request):
        return render(request, "bills_edit.html",)
    


class VendorsView(View):
    def get(self, request):
        vendor = Vendor.objects.all()
        paginator = Paginator(vendor,8)
        pagenumber =request.GET.get('page')
        vendor= paginator.get_page(pagenumber)
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

    

def upload_vendor_csv(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        print("----------------file",file)
        if not file :
            messages.error(request, "No file uploaded. Please select a file to upload.")   
            return render(request, 'uploadfile.html')     
        filename, file_extension = os.path.splitext(file.name)
        if file_extension  not in [".xlsx",".csv",]:
            messages.error(request, "Please upload in one of these vaild file formats -  xlsx or csv ")
            return render(request, 'uploadfile.html')
    
        data = pd.read_excel(file)
        # Iterate through the rows of the DataFrame
        for index, row in data.iterrows():
            # Access data from each column for the current row
            name = row['name']
            email = row['email']
            phone = row['phone']
            
            Vendor.objects.create(name=name,email=email,phone=phone,)
        return redirect("vendors")
    
    return render(request, "vendors.html")