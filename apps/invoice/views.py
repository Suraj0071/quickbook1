from django.shortcuts import render
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
                Customer.objects.create(name = name, email=email , phone=phone , first_name= first_name, last_name = last_name)
            if companyname:
                Business.objects.create( name = companyname , address1=address1 , address2=address2, city=city,zip_code=zip, country=country,
                                        state = state, phone=phone,fax=fax,mobile=mobile,website=website)
                
            if invoice_title:
                invoice = Invoice.objects.create(title= invoice_title,description=invoice_description, invoice_number=invoice_number,invoice_date=invoice_date ,paymnet_due=payment_due,
                                    footer_text= footer )
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
        return render(request, "customer_statements.html")
    

class CustomersView(View):
    def get(self, request):
        return render(request, "customers.html")
    


class Products_servicesView(View):
    def get(self, request):
        return render(request, "products_services.html")
    


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


