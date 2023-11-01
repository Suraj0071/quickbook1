from django.shortcuts import render ,redirect
from django.views import View
from apps.invoice.models import *
from io import BytesIO
from django.http import HttpResponse 
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
# Create your views here.
from apps.invoice.utils import render_to_pdf,save_item
from weasyprint import HTML
from django.template.loader import render_to_string
from . email import *

from . forms import *

class InvoicesView(View):
    def get(self, request):
        return render(request, "Invoices.html")
    

class create_invoice(View):
    def get(self, request):
        customer = Customer.objects.all()
        business= Business.objects.all()
        context = {
            "customer":customer,
            "business": business

        }
        return render(request, "create_invoice.html",context)
    def post(self, request):
        try:
            itemname= request.POST.getlist('itemname')
            quantity= request.POST.getlist('quantity')

            price= request.POST.getlist('price')
            customer = request.POST.get('customer')
            business = request.POST.get('business')
            name = request.POST.get('cusName')
        
            email = request.POST.get('cusEmail')
            phone = request.POST.get('cusphone')
            first_name = request.POST.get('firstname')
            last_name =  request.POST.get("lastname")
            companyname = request.POST.get('companyname')
        
            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            city = request.POST.get('city')
            zip = request.POST.get('zip')
            country = request.POST.get('country')
            state = request.POST.get('state')
            phone = request.POST.get('phone')
            fax = request.POST.get('fax')
            mobile = request.POST.get('mobile')
            website = request.POST.get('website')
            invoice_title =  request.POST.get("invoice_title")
            invoice_description =  request.POST.get("invoice_description")
            invoice_number  = request.POST.get("invoice_number") 
            invoice_date  = request.POST.get("invoice_date")
            payment_due  = request.POST.get("payment_date") 
            footer  = request.POST.get("invoice_footer") 
            
            if name:
                obj =Customer.objects.create(name = name, email=email , phone=phone , first_name= first_name, last_name = last_name)
                Billing_Address.objects.create(customer=obj)
                Shipping_Address.objects.create(customer=obj)

            if companyname:
                Business.objects.create( name = companyname , address1=address1 , address2=address2, city=city,zip_code=zip, country=country,
                                        state = state, phone=phone,fax=fax,mobile=mobile,website=website)
            if invoice_title:
                invoice = Invoice.objects.create(title= invoice_title,customer_id=customer,description=invoice_description, invoice_number=invoice_number,invoice_date=invoice_date ,paymnet_due=payment_due,
                                    footer_text= footer)
                customer = Customer.objects.filter(id = customer).first()
            
                business= Business.objects.filter(id=business).first()
                
                total = save_item(itemname,quantity,price,customer)
                amount = total["amount"]

                items = []

                for i in range(len(itemname)):
                        item = {
                            "name": itemname[i],
                            "qty": quantity[i],
                            "price": price[i],
                            "amount": amount[i]
                        }
                        items.append(item)
                context = {'items': items,
                        "total":total["alltotal"],
                        "amount_paid":total["amount_paid"],
                        "customer":customer,
                        "business": business,
                        "invoice" :invoice

                        }

                html_string = render_to_string('invoice_pdf.html', context)

                pdf = HTML(string=html_string).write_pdf()
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="output.pdf"'

                return response
            return render(request, "Invoices.html")

            # pdf = render_to_pdf('invoice_pdf.html', context)
            #return HttpResponse(pdf, content_type='application/pdf')

            # force download
            # if pdf:
            #     response = HttpResponse(pdf, content_type='application/pdf')
            #     # filename = "Invoice_%s.pdf" %(context['pos_so_num'])
            #     filename = f"invoice{pos_so_num}.pdf"
            #     content = "inline; filename='%s'" %(filename)
            #     #download = request.GET.get("download")
            #     #if download:
            #     content = "attachment; filename=%s" %(filename)
            #     response['Content-Disposition'] = content
            #     return response
        except Exception as e:
            print("This  is exception",e)
            return HttpResponse("-------------------")
            






class Customer_statementsView(View):
    def get(self, request):
        customer = Customer.objects.all()
        context = {
            "customer":customer
        }
        return render(request, "customer_statements.html",context)
    
    def post(self, request):
        customer= request.POST.get('customer')
        type= request.POST.get('type')
        from_date= request.POST.get('from')
        to_date= request.POST.get('to')
        
        print(f"-------------{customer} {type}  {from_date}   {to_date}")

class CustomersView(View):
    def get(self, request):
        customer = Customer.objects.all()
        context = {
            "customer":customer
        }
        return render(request, "customers.html",context)
    

class Create_customervew(View):
    def get(self, request):
        customer = Customer.objects.all()
        context = {
            "customer":customer
        }
        return render(request, "customers_add.html",context)
    def post(self,request):
        name= request.POST.get('name')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        account_number= request.POST.get('account_number')
        notes= request.POST.get('notes')
        website= request.POST.get('website')
        currency= request.POST.get('currency')
        address1= request.POST.get('address1')
        address2= request.POST.get('address2')
        country= request.POST.get('country')
        city= request.POST.get('city')
        postal= request.POST.get('postal')
        ship_to= request.POST.get('ship_to')
        ship_address1= request.POST.get('ship_address1')
        ship_address2= request.POST.get('ship_address2')
        ship_country= request.POST.get('ship_country')
        ship_city= request.POST.get('ship_city')
        ship_postal= request.POST.get('ship_postal')
        if name:
            obj = Customer.objects.create(name=name,first_name=first_name, last_name=last_name,email=email,phone=phone,account_number=account_number,
                                    notes=notes,website=website)
        if currency:
            Billing_Address.objects.create(currency=currency,address1=address1,address2=address2,country=country,city=city,postal=postal,customer=obj)

        if ship_to:
            Shipping_Address.objects.create(customer=obj,ship_to = ship_to,address1= ship_address1 , address2=ship_address2 ,country=ship_country,city=ship_city,postal=ship_postal)

        return redirect("customers")
    

def edit_customer(request,id):
    customer = Customer.objects.get(id=id)
    billing = Billing_Address.objects.get(customer=id)
    shipping = Shipping_Address.objects.get(customer=id)
    context = {
        "customer":customer,
        "billing" : billing,
        "shipping" :shipping,
    }
    if request.method == "POST":
        response = Customer.objects.get(id=id)
        billing = Billing_Address.objects.get(customer=id)
        shipping = Shipping_Address.objects.get(customer=id)
        response.first_name  =  request.POST['first_name']
        response.last_name  =  request.POST['last_name']
        response.email  =  request.POST['email']
        response.phone  =  request.POST['phone']
        response.account_number  =  request.POST['account_number']
        response.notes  =  request.POST['notes']
        response.website  =  request.POST['website']

        billing.currency= request.POST.get('currency')
        billing.address1= request.POST.get('address1')
        billing.address2= request.POST.get('address2')
        billing.country= request.POST.get('country')
        billing.city= request.POST.get('city')
        billing.postal= request.POST.get('postal')
        
        shipping.ship_to= request.POST.get('ship_to')
        shipping.address1= request.POST.get('ship_address1')
        shipping.address2= request.POST.get('ship_address2')
        shipping.country= request.POST.get('ship_country')
        shipping.city= request.POST.get('ship_city')
        shipping.postal= request.POST.get('ship_postal')
        response.save()
        billing.save()
        shipping.save()
        return redirect("customers")
    return render(request, "customers_edit.html",context)


def delete_customer(request,id):
    obj = Customer.objects.filter(id=id).first()
    print("0----------------------",obj)
    obj.delete()
    return redirect("customers")


class Products_servicesView(View):
    def get(self, request):
        return render(request, "products_services.html")
    



class Tax_create(View):
    def get(self, request):
        tax = Tax.objects.all()
        context = {
            "taxes": tax
        }
        return render(request, "products_services_add.html",context)
    def post(self,request):


        
        return redirect("products-services")
    
    

def edit_tax(request,id):
    customer = Tax.objects.get(id=id)
  
    context = {
        "tax":customer,
        
    }
    if request.method == "POST":
        response = Tax.objects.get(id=id)
       
        response.save()
        
        return redirect("products-service")
    return render(request, "products_services_edit.html",context)




def delete_tax(request,id):
    obj = Tax.objects.filter(id=id).first()
    print("0----------------------",obj)
    obj.delete()
    return redirect("products-service")









class BillsView(View):
    def get(self, request):
        return render(request, "bills.html")
    


class VendorsView(View):
    def get(self, request):
        return render(request, "vendors.html")



class TransactionsView(View):
    def get(self, request):
        return render(request, "transactions.html")
    

class ReconciliationView(View):
    def get(self, request):
        return render(request, "reconciliation.html")


class Chart_of_AccountsView(View):
    def get(self, request):
        return render(request, "chart_of_accounts.html")
    







class  Financial_Statements_View(View):
    def get(self, request):
        return render(request, "financial_statements.html")



class TaxexView(View):
    def get(self, request):
        return render(request, "taxes.html")

class Repport_CustomersView(View):
    def get(self, request):
        return render(request, "report_customers.html")
    


class Account_TransactionsView(View):
    def get(self, request):
        return render(request, "account _transactions.html")


